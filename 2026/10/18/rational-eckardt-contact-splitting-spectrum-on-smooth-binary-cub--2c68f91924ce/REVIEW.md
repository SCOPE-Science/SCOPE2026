# Self-review

## Correctness — PASS

Exhaustive group-action enumeration covers all 1,048,575 binary cubic coefficient masks. A second Burnside count independently verifies 141 nonzero projective orbits. Four projective charts and unit-ideal Gröbner criteria verify geometric smoothness, giving 36 smooth orbits and 322,560 equations. Independent symbolic tangent-section arithmetic and separate line-containment tests agree on rational Eckardt incidence, Frobenius splitting types and the 21 weighted strata. See `code/reproduce.py` and `data/` for exact replay; no general finite-field or infinite extrapolation is made.

## Originality — PASS (residual priority risk)

Dolgachev–Duncan, *Automorphisms of cubic surfaces in positive characteristic* (arXiv:1712.01167), treat geometric Eckardt configurations; Kadyrsizova et al., *Cubic Surfaces of Characteristic Two* (arXiv:2007.12018), treat characteristic-two Frobenius splitting and tritangent geometry; Das, *Arithmetic statistics on cubic surfaces* (arXiv:2002.11183), provides rational-point and Frobenius-line permutation data; Betten (ICMS 2018, DOI:10.1007/978-3-319-96418-8_7) limits his finite catalog to surfaces with 27 rational lines, none at q=2. Frobenius-stable line trios are not necessarily concurrent. Previously established totals of 36 smooth projective classes and the 15-Eckardt symplectic example are background, not claims of priority. Inspected material and mathematical record searches did not yield the 21-stratum weighted rational Eckardt Frobenius-contact table. An unindexed prior table or unpublished computation could already contain it; independent priority review is still needed.

## Value — PASS

Concurrence of the three geometric tangent lines and their rationality types are natural incidence invariants, independently refining the point count and geometric Eckardt strata. For example, curves with nine rational points can have 0, 1, 2 or 4 rational Eckardt contacts. The full weighted classification distinguishes natural arithmetic configurations not implied by the broader published counts.

## Limitations

Only embedded cubic equations over the binary field are classified under rational projective changes of coordinates; no larger-field statement or abstract-isomorphism census is claimed. Verification is reproducible but is not an independent expert audit. The principal residual scientific risk is an earlier unindexed equivalent enumeration.

Self-review: passed. Independent audit: not yet performed.
