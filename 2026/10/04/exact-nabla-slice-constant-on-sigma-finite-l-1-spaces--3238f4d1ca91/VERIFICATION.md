---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For \(0<m(f)<1\), positive atomic mass has a maximizing atom because infinitely many distinct atoms carrying a fixed positive fraction of the supremum would contradict \(\|f\|_1=1\). The slice supported on such an atom and cut exactly at mass \(m(f)\) avoids \(f\), has every point at distance at most \(2(1-m(f))\), and an explicit sign-reversed remainder vector attains that distance. Conversely, for any avoiding slice, the high-level set of its \(L_\infty\) functional has positive measure. If it contains an atom, the normalized signed atomic vector lies in the slice and is at distance at least \(2(1-m(f))\); if it contains no atom, sigma-finiteness and atomlessness provide a finite-measure subset with arbitrarily small \(|f|\)-mass, giving slice points with distance tending to two. The endpoint \(m(f)=0\) therefore gives two. If \(m(f)=1\), \(f\) is exactly a signed normalized atom; an avoiding slice cannot have its high-level atom aligned with \(f\), while any other atomic or atomless high-level witness is at distance two. This proves the discontinuous endpoint and the full formula. The exact-rational finite-atomic verifier exercises the slice geometry but is not used as a proof of the sigma-finite theorem.

## originality

PASS

Haller et al. introduce \(
abla\)-points by exactly the avoiding-slice condition and prove the qualitative scalar \(L_1\) classification: atom-free support gives the Daugavet/\(
abla\) behavior, while if the support contains an atom the only \(
abla\)-points are signed normalized atomic indicators. Choi and Jung quantify different slice families: their Daugavet constant takes all slices and their Delta constant takes slices containing the point; in atomic \(L_1\) they obtain \(2-2m\), and in \(\ell_1\) both of those constants equal \(2-2\|x\|_\infty\). These results explain why the new avoiding-slice constant agrees numerically in the interior but do not imply its endpoint \(m=1\), where the prior Daugavet/Delta constants are zero while the audited constant is two, nor do they state the mixed atomic/nonatomic sigma-finite formula. Current Resultary search found neighboring Daugavet-constant work but no quantitative avoiding-slice formula.

## value

PASS

Quantifying an established diametral notion by taking the exact infimum over its defining avoiding slices is natural, and the formula reveals behavior not visible from the older constants: mixed atomic/nonatomic points are controlled solely by their largest atomic mass, while the normalized-atom endpoint jumps back to two. This completes the scalar \(L_1\) geometry of the newly introduced \(
abla\) notion and supplies an exact \(\ell_1\) benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
