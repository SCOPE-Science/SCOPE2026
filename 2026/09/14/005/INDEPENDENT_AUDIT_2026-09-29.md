# Independent audit — 2026-09-29

Record: `2026/09/14/005`  
Audited source tree: `362529cef0af4b33105b0e162ebfacd5a672018f`  
Disposition: **repaired**

## Correctness

The empty Case-1 locus is correct. For the normalized invariant s=p'/2+p^2/4-r, the finite double-pole coefficients at 0,1,2 are all -3/16 and the coefficient at infinity is -1/4, independently of q. Kovacic Case 1 therefore has finite alpha choices {1/4,3/4} and the singleton alpha_infinity={1/2}; every candidate degree 1/2-(alpha_0+alpha_1+alpha_2) is one of -1/4,-3/4,-5/4,-7/4. Hence no q yields a rational Riccati solution or reducible/Borel Case-1 solution. The repair does not change the theorem; it corrects the artifact path and removes the unsupported statement that this reducible locus was previously unknown.

## Originality

The Lamé family with local exponents ±1/4 and its reducible locus were studied explicitly by Loray, van der Put, and Ulmer. The audited t=2, alpha=beta=1/4 slice is therefore best presented as an explicit specialization and uniform Kovacic certificate within established Lamé differential-Galois theory, not as a new family-level reducibility classification.

## Scientific value

The calculation gives a short, exact, q-uniform certificate that the entire named accessory line has empty reducible locus. Its value is reproducibility and clarity for this concrete slice rather than novelty of the surrounding Lamé-family theory.

## Limitations

- The theorem classifies only Kovacic Case 1; special q values in Cases 2 or 3 are outside the claim.
- The result is only the t=2 symmetric half-exponent slice, not a new classification of the full Lamé or Heun family.
- Prior Lamé-family reducibility literature means the record must not claim that the finite reducible q-locus was previously unknown.
- The archived script is stored at artifacts/kovacic_case1_normalform.py, not output/artifacts/kovacic_case1_normalform.py as the original research text stated.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/005
- https://numdam.org/articles/10.5802/afst.1187/
- https://doi.org/10.1016/S0747-7171(86)80010-4
- https://dlmf.nist.gov/31.2
- https://dlmf.nist.gov/31.8
