# Independent Audit — 2026/09/13/044

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `b9ad74822c3c96366d72de98478fa35e2ec6de82`
- Disposition: **PASSED**

## Correctness

**PASS** — The trichotomy follows from exact 2-adic valuation algebra. The critical points are 0 and infinity, and {1,infinity} is a superattracting 2-cycle. If m=v2(a)>=1, the disk v2(z)>=m is invariant and the exact difference formula gives contraction factor at most 2^{-m}, hence a unique attracting fixed point containing the orbit of 0. If m<=0, E_a(z)-1=(a+1)/(z^2-1) alternates large points with points near 1; once near 1, v2(z^2-1)=v2(z-1)+1 (with the first borderline step handled directly), and the two-step recurrence strictly increases the proximity to 1. The exceptional pole hits are finite captures into {1,infinity}. Thus both critical points are attracted to attracting cycles for every admissible a. The supplied exact-rational script is consistent with, but is not needed in place of, this general valuation proof.

## Originality

**PASS** — The cited non-archimedean literature explains why wild recurrent critical points matter for wandering domains, but it does not supply this all-parameter orbit classification for the specific bicritical family (z^2+a)/(z^2-1). The result is not a formal restatement of Rivera-Letelier or Benedetto: the substantive content is the uniform valuation recurrence and contraction split across all a in Q_2.

## Scientific value

**PASS** — A complete critical-orbit classification for a one-parameter residue-characteristic-2 family is a reusable structural lemma. It proves uniform hyperbolicity and eliminates the wild-recurrent-critical mechanism across the whole family, materially narrowing any later wandering-domain analysis even though it does not itself prove the full no-wandering theorem.

## Sources

- Wild recurrent critical points (Juan Rivera-Letelier): https://arxiv.org/abs/math/0406417 — Shows the central role of wild recurrent critical points in possible p-adic wandering phenomena.
- Wandering domains and nontrivial reduction in non-archimedean dynamics (Robert L. Benedetto): https://arxiv.org/abs/math/0312034 — Background on wandering domains and reduction; it does not compute the present family's critical orbits.

## Limitations

- Passing this record does not upgrade the result to a proof that every Berkovich Fatou component is preperiodic.
- The originality conclusion is for the explicit family-wide trichotomy, not for the general principle linking recurrence and wandering.

GitHub was read only as evidence. Open-access/preprint sources were checked first; no Oxford Download was needed in this run.
