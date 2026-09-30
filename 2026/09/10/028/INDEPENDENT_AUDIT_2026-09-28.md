# Independent Audit — 2026/09/10/028

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `98a3b20ee2190d0304548e39f3a3399e902df3a6`  
**Audited current source tree:** `98a3b20ee2190d0304548e39f3a3399e902df3a6`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA, so no intervening record change required a stale-source re-audit.

## Correctness

PASS. I independently evaluated the Brill--Lindquist formulas on S_{r=10}. Dense direct quadrature gives min H_g≈0.1548304900, J1≈2.4358933583, J2≈0.06538684547, A≈1530.51694, I/(16π)≈0.8173355684, and m_H≈1.0079480105, all comfortably inside the claimed theorem-level bounds min H>=0.10 and m_H in [0.96,1.06], and centered in the record's tighter certified intervals. I also inspected the interval code: it uses rational interval operations, outward square-root enclosures, and 400 c-panels, so the broad theorem bounds are genuinely enclosed rather than inferred from point sampling. The conditional area inequality A(Σ_out)<=16π(1.01)^2 is the standard time-symmetric Riemannian Penrose inequality for an outermost/outer-minimizing minimal horizon; the r=10 anchor is not needed to strengthen that ADM bound, and the RESULT correctly says its finite-radius Hawking-mass upper bound is not used for the cap.

## Originality

SUPPORTED AS A RECORD-SPECIFIC CERTIFICATE. Brill--Lindquist data and the Riemannian Penrose inequality are classical. The contribution here is the explicit, rigorously enclosed finite-radius Hawking-mass/outer-untrapped certificate for the fixed (1,0.01,d=3,r=10) cell. A targeted exact-parameter search did not reveal a prior source with this numerical certificate; that search absence is not treated as a proof of broad novelty.

## Scientific value

MODEST BUT REAL COMPUTATIONAL VALUE. The certified sphere gives a reproducible outer-untrapped and quasi-local-mass anchor useful for later horizon/IMCF investigations of this fixed extreme-ratio data set. It does not resolve the harder outermost-horizon pin/gap problem, as the record explicitly states.

## Limitations

- I independently reconstructed the central values and inspected the rigorous interval implementation, but did not reproduce a formal proof assistant certificate.
- The area corollary is conditional on the stated outermost/outer-minimizing horizon hypothesis and is not a bound for arbitrary enclosed MOTS.
- The finite-radius anchor is a specialized numerical certificate, not a general Brill--Lindquist theorem.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/028
- https://doi.org/10.4310/jdg/1090349447
- https://doi.org/10.1103/PhysRev.131.471
