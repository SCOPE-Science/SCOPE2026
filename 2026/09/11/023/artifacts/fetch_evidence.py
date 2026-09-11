"""Evidence harvest for lane-716 (stdlib only, bounded timeouts).

Fetches three independent published sources and writes:
  evidence_hap_bogomolov.md      - HAP official docs: Moravec isoclinism-invariance
                                   theorem + exhaustive B0 census output
  evidence_jena_hs_table.json    - Jena cohomology catalogue Hall-Senior numbers
                                   for anchor (64,199) + the nine HAP B0-positive IDs
  evidence_groupprops_isoclinism.txt - Groupprops: isoclinic = Hall-Senior families,
                                   27 classes at order 64
Run: python3 fetch_evidence.py  (writes files next to itself, prints log)
"""
import json
import re
import urllib.request

UA = {"User-Agent": "lane716-scope-evidence/1.0 (research harvest; contact: n/a)"}
TIMEOUT = 20

B0_IDS = [149, 150, 151, 170, 171, 172, 177, 178, 182]
ANCHOR = 199


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.status, r.read().decode("utf-8", errors="replace")


def strip_tags(html):
    t = re.sub(r"<script.*?</script>", " ", html, flags=re.S)
    t = re.sub(r"<style.*?</style>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return " ".join(t.split())


def main():
    print("=== lane-716 evidence harvest ===")

    # ---- Source 1: HAP official Bogomolov page ----
    st, hap = get("https://gap-packages.github.io/hap/www/SideLinks/"
                  "About/aboutBogomolov.html")
    print(f"HAP page HTTP {st}, {len(hap)} chars")
    text = strip_tags(hap)
    assert "Primoz Moravec has observed" in text, "invariance context missing"
    assert ("If G is isoclinic to H then B 0 (G) is isomorphic to B 0 (H)"
            in text), "invariance theorem sentence missing"
    for nid in B0_IDS:
        assert f"[ 64, {nid} ]" in text, f"HAP census missing [64,{nid}]"
    assert "[ 64, 199 ]" not in text, "anchor unexpectedly in HAP page IDs"
    i = text.find("Primoz Moravec has observed")
    j = text.find("NonTrivial; [ [ 64, 149 ]")
    with open("evidence_hap_bogomolov.md", "w") as f:
        f.write("# HAP official docs excerpt (About: The Bogomolov Multiplier)\n")
        f.write("# URL: https://gap-packages.github.io/hap/www/SideLinks/About/aboutBogomolov.html\n\n")
        f.write("## Moravec isoclinism-invariance theorem (verbatim, tags stripped)\n\n")
        f.write(text[i - 260:i + 260].replace("&nbsp;", " ").replace("&gt;", ">") + "\n\n")
        f.write("## Exhaustive census code + output head (verbatim)\n\n")
        f.write(text[j - 700:j + 700].replace("&nbsp;", " ") + "\n")
    print("wrote evidence_hap_bogomolov.md")

    # ---- Source 2: Jena cohomology catalogue HS numbers ----
    table = {}
    for gid in [ANCHOR] + B0_IDS:
        st, d = get(f"https://users.fmi.uni-jena.de/~green/Coho_v3/64gps/64gp{gid}.html")
        t = strip_tags(d)
        m = re.search(r"Hall-Senior number of this group is (\d+)", t)
        g = re.search(r"G has (\d+) minimal generators, rank (\d+) and exponent (\d+)", t)
        assert m, f"no HS number on Jena page 64gp{gid}"
        table[str(gid)] = {"hs": int(m.group(1)),
                           "generators": list(map(int, g.groups())) if g else None,
                           "url": f"https://users.fmi.uni-jena.de/~green/Coho_v3/64gps/64gp{gid}.html"}
        print(f"Jena 64gp{gid}: HS={m.group(1)} gen={g.groups() if g else '?'}")
    with open("evidence_jena_hs_table.json", "w") as f:
        json.dump({"anchor_id": ANCHOR, "b0_positive_ids": B0_IDS, "groups": table}, f, indent=2)
    hs_block = sorted(v["hs"] for k, v in table.items() if k != str(ANCHOR))
    assert hs_block == list(range(225, 234)), f"nine HS numbers not the 225-233 block: {hs_block}"
    assert table[str(ANCHOR)]["hs"] == 106
    print("wrote evidence_jena_hs_table.json; nine B0 IDs <-> HS block 225..233 exact; anchor HS=106")

    # ---- Source 3: Groupprops order-64 page ----
    st, gp = get("https://groupprops.subwiki.org/wiki/Groups_of_order_64")
    t = strip_tags(gp)
    k = t.find("isoclinic groups")
    assert k > 0, "isoclinism section missing"
    with open("evidence_groupprops_isoclinism.txt", "w") as f:
        f.write("# Groupprops 'Groups of order 64' excerpt\n")
        f.write("# URL: https://groupprops.subwiki.org/wiki/Groups_of_order_64\n\n")
        f.write(t[k - 100:k + 1500] + "\n")
    print("wrote evidence_groupprops_isoclinism.txt")

    print("=== harvest OK: all assertions passed ===")


if __name__ == "__main__":
    main()
