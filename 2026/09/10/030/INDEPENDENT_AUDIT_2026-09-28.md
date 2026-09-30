# Independent Audit — 2026/09/10/030

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `86418c682e7d68de32ae4f31792dffaed2b03cf4`  
**Audited current source tree:** `86418c682e7d68de32ae4f31792dffaed2b03cf4`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA, so no intervening record change required a stale-source re-audit.

## Correctness

PASS. The algebraic-arc contradiction is valid. On a dominant real-algebraic arc, normalization gives local algebraic germs x(s),z(s). The constant-z case reduces e^x to a polynomial in x; differentiating on a nonconstant germ forces a second polynomial identity and hence x constant, contradiction. In the both-nonconstant case M=C(x,z) has trdeg 1; the defining equation makes e^x algebraic over M(℘(z)) and ℘'(z) is algebraic over ℘(z), so C(x,z,e^x,℘(z),℘'(z)) has trdeg at most 2. Apply Ax's analytic-subgroup/Ax--Schanuel theorem to the semi-abelian variety G_m×E0: because Hom(G_m,E0)=Hom(E0,G_m)=0, a germ with both coordinates nonconstant is not contained in a translate of a proper connected algebraic subgroup, so the expected one-parameter lower bound is dim(G_m×E0)+1=3. This contradicts the upper bound. A modern open-access semi-abelian Ax--Schanuel reference explicitly states the n+1 transcendence-degree lower bound and attributes the formal-power-series theorem to Ax (1972). The record's Gao citation is broader than necessary, but the needed black box is standard and available directly in the semi-abelian setting.

## Originality

SUPPORTED AS A SPECIALIZED APPLICATION, NOT A NEW AX--SCHANUEL THEOREM. The functional-transcendence input is classical/general. The record specializes it to one fixed exp-plus-polynomial/Weierstrass cell and observes that the degree bound is unnecessary. A targeted exact-equation search did not show this particular cell in prior literature; that absence is not itself taken as a novelty proof.

## Scientific value

USEFUL FALLBACK LEMMA. The result cleanly removes all dominant algebraic curves from the algebraic locus of the fixed cell, which is a meaningful prerequisite for later Pila--Wilkie counting. It does not establish the requested log-power counting exponent, and the record clearly limits itself to the locus exclusion.

## Limitations

- The semi-abelian Ax--Schanuel theorem is used as an external black box.
- The cited Gao universal-abelian-variety paper is not the most direct citation for G_m×E; Ax 1972 / modern semi-abelian formulations are the cleaner support.
- No quantitative Pila--Wilkie counting bound follows from this lemma alone.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/030
- https://doi.org/10.2307/2373569
- https://arxiv.org/abs/2203.00470
- https://arxiv.org/abs/1806.01408
