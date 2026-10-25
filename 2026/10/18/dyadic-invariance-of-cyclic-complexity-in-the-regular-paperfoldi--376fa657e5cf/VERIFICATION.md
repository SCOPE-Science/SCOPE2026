---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With 1-indexed odd-part-residue f, f_{2t}=f_t and every odd global position alternates with the next odd one. A full factor cannot be alternating for four symbols, since any two same-parity odd global positions distance 2 have opposite bits. For every even factor of length ≥8, precisely one of its two tracks alternates, while the other is a length-≥4 factor of f, giving intrinsic occurrence-start parity. When n≡0 mod4, its alternating track has even length and cyclic rotations preserve alternation; rotating a factor by r changes its occurrence parity by r mod2. Interleave an n-factor f_t... with alternating f_{2(t+j)+1} to obtain a genuine 2n-factor at 2t. Any factor beginning at 2t−1 is a one-symbol cyclic rotation of this lift, by 2n-periodicity of odd-position bits mod4. The map is surjective on all 2n-factor conjugacy classes, equivariant under even lifted rotations, and injective because an odd rotation would exchange unique alternating and nonalternating tracks. Independent 16,384-symbol enumeration found the known exhaustive 4ℓ distinct factors at each ℓ=n,2n and independently counted seven pairs (n,2n) for n=8,12,16,20,24,28,32. It reproduced c4=3,c8=4,c12=16,c20=28,c28=40. Finite checks were exhaustive only at tested lengths using Allouche p(ℓ)=4ℓ; the bijection proves all n≥8 divisible by four.

## originality

PASS

The original Cassaigne–Fici–Sciortino–Zamboni paper proves for all paperfolding words that the special power-of-two ray c(4*2^{j})=4 for j≥1; this is acknowledged and is covered prior work. Its complete Proposition 20 has length 4*2^{n+1}, not every multiple 4r of arbitrary odd r, and does not yield the exhibited canonical one-to-one orbit decimation for all such n. Krawchuk–Rampersad 2018 examines cyclic complexity largely for Fibonacci and Thue–Morse words rather than the regular paperfolding arbitrary-multiplier doubling theorem. The new accepted statement is the much broader classwise invariant for all n≥8,4|n, not the known ray or baseline factor formula.

## value

PASS

A scale-invariance bijection for an entire infinite congruence class of factor lengths explains structural self-similarity of cyclic rotation equivalence, rather than a single constant power-of-two ray or isolated finite sequence values. The sharp n=4 failure clarifies the natural boundary. The nontrivial arbitrary-odd-multiplier extension supplies new exact cyclic class counts along infinitely many dyadic rays.

The dated certificate retains the supplied scientific assessment, sources and limitations.
