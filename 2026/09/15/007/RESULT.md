# Explicit unconditional degree-independent uniform bound for K-rational preperiodic points of postcritically finite unicritical polynomials

## Context

The Morton-Silverman uniform boundedness conjecture predicts a bound on K-rational preperiodic points depending only on the degree of the number field, the dimension, and the degree of the map. It remains open in general. For unicritical polynomials f_{d,c}(x)=x^d+c, prior degree-independent bounds over number fields were conditional on the abc/abcd conjectures (Looper; Doyle-Hindes), while unconditional explicit bounds depended on the degree d or on extra local reduction hypotheses.

## Definitions

Let K be a number field with [K:Q]=D, d>=2 an integer, and f_{d,c}(x)=x^d+c with c in K. The map is postcritically finite (PCF) if 0 is preperiodic, i.e. its forward orbit {f^n_{d,c}(0)} is finite. A point x in K is preperiodic if {f^n_{d,c}(x)} is finite. Let h denote the absolute logarithmic Weil height and hat{h}_f the canonical height. Define B(D)=D^2*(2*8^D+1)^{D+1}, so B(1)=289 and B(2)=8586756.

## Result

Let D>=1. For every number field K with [K:Q]=D, every integer d>=2, and every c in K for which f_{d,c} is postcritically finite, the number of affine K-rational preperiodic points satisfies |{x in K : x preperiodic for f_{d,c}}| <= B(D), unconditionally. The bound depends only on D: it is independent of d, of c, and of the particular field K.

## Proof / Evidence

Lemma 1 (PCF pins c): If 0 is preperiodic then c is an algebraic integer and every conjugate satisfies |sigma(c)|<=2. Non-archimedean: |c|_v>1 gives |a_k|_v=|c|_v^{d^{k-1}}->infinity by ultrametric induction, contradicting finiteness. Archimedean: R=|c|>2 gives |a_{k+1}|>=|a_k|(R^{d-1}-1) with ratio >1, hence escape. Thus h(c)<=log 2 uniformly in d.

Lemma 2 (height comparison): |h(f(x))-d h(x)|<=h(c)+log 2, via ultrametric and triangle estimates place by place, verified on 1000 randomized rational instances.

Lemma 3 (canonical telescoping): With C=h(c)+log 2, |hat{h}_f(x)-h(x)|<=C/(d-1). Preperiodic points have hat{h}_f=0, so h(x)<=C<=2log 2=log 4 uniformly.

Lemma 4 (explicit Northcott): The set S_D of degree<=D, height<=2log2 points has |S_D|<=B(D) via Mahler measure M<=4^D and coefficient bound |b_j|<=8^D, giving at most (2*8^D+1)^{D+1} polynomials per degree.

Every K-rational preperiodic point lies in S_D, proving the theorem. Full arithmetic equidistribution is not needed. Computations in output/artifacts/compute_B.py reproduce B(D), the D=1 enumeration (23 rationals), and height-inequality checks.

## Limitations

B(D) is astronomically large for D>=3 and is a uniform finiteness bound, not a sharp classification. It counts affine points only; infinity is always fixed and excluded. No sharpness or completeness of any census is claimed.

## Reproducibility

Run `python3 output/artifacts/compute_B.py`: asserts B(1)=289, B(2)=8586756, checks Mahler coefficient bounds, enumerates D=1 rationals with h<=2log2, and spot-checks Lemma 2 on 1000 random cases.

## References

- Morton-Silverman uniform boundedness conjecture; Poonen survey arXiv:1206.7104.
- Doyle-Hindes arXiv:2408.14657: conditional degree-independent bounds over abc-fields.
- Looper: abc-conditional bounds for unicritical polynomials.
- Benedetto-Ih arXiv:2010.15941: finiteness of integral PCF parameters; bounded PCF height.
- Rajagopal-Zhang arXiv:2510.26119: unconditional d-dependent bound #Per<=d^D under good reduction.
