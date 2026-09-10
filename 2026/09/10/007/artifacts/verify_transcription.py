"""Transcription audit: parse k0_paper.tex for the Thm-2 minimal-nonface list
and compare against the hardcoded transcription used by all verifiers.

Closes the transcription-error loophole: the obstruction stands or falls on
the exact 15-item list, so this script extracts it from the downloaded
arXiv e-print source (li-pa22-01-29.tex) independently of manual copying.
Repro: python3 verify_transcription.py. Stdlib only.
"""
import re
from pathlib import Path

import verify_target_obstruction as V

tex = (Path(__file__).parent / "k0_paper.tex").read_bytes().decode("latin-1")
anchor = tex.find("minimal non-faces:")
assert anchor != -1, "anchor 'minimal non-faces:' not found in TeX source"
end = tex.find(". Then", anchor)
assert end != -1, "end anchor '. Then' not found"
region = tex[anchor:end]
print("REGION_EXCERPT:", region[:160].replace("\n", " "), "...")

found = re.findall(r"\((\d+(?:,\d+)+)\)", region)
parsed = [tuple(int(x) for x in t.split(",")) for t in found]
print(f"PARSED_COUNT = {len(parsed)}")
for t in parsed:
    print("  parsed:", t)

expected = V.MIN_NONFACES_1
print(f"EXPECTED_COUNT = {len(expected)}")
assert len(parsed) == 15, f"expected 15 items in source region, got {len(parsed)}"
assert len(parsed) == len(expected)
if parsed == expected:
    print("ORDERED_MATCH: parsed list equals hardcoded transcription in order")
else:
    print("NOTE: order differs; checking set equality...")
assert set(parsed) == set(expected), (
    f"SET MISMATCH: only-in-source={set(parsed)-set(expected)}, "
    f"only-in-code={set(expected)-set(parsed)}")
print("SET_MATCH: parsed source list equals hardcoded transcription as sets")
# every parsed item length >= 3 (supports full 1-skeleton lemma input)
assert all(len(t) >= 3 for t in parsed)
print("TRANSCRIPTION_AUDIT_PASS")
