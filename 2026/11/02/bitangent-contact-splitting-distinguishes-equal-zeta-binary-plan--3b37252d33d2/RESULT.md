# Bitangent contact splitting distinguishes equal-zeta binary plane quartics

## Finding

Let \(C\) vary through all geometrically smooth plane quartic curves over \(\mathbb F_2\), taken up to \(\mathbb F_2\)-isomorphism. For each curve let \(P_C(T)\) be its degree-six Hasse–Weil zeta numerator. For each \(\mathbb F_2\)-rational line \(L\) satisfying \(C\cdot L=2D\) geometrically, with \(\deg D=2\), classify \(D\) by its rational support: a conjugate quadratic pair (type 0), one rational point twice (type 1, hyperflex), or two distinct rational points (type 2). Let \(\theta(C)=(n_0,n_1,n_2)\) count lines of these respective types.

Among the \(78\) isomorphism classes of smooth plane quartics over \(\mathbb F_2\), exactly \(73\) distinct zeta numerators occur, with precisely five repeated numerators (each occurring for two classes). The joint invariant \((P_C,\theta(C))\) takes exactly \(75\) distinct values. Exactly two of the five equal-zeta pairs have different rational bitangent-contact splitting. In both, the two curves even have the same total number (one) of rational bitangent lines. Thus the Weil polynomial and number of rational bitangents together do not determine contact splitting.

One such pair has canonical monomial masks 4249 and 4469 (defined below). Both have \(P(T)=1-T+T^2+2T^4-4T^5+8T^6\), but their contact signatures are \((0,1,0)\) and \((1,0,0)\), respectively. Another pair, masks 4347 and 4415, share \(P(T)=1+3T^3+8T^6\), with signatures \((0,1,0)\) and \((0,0,1)\). These four curves are distinct even as abstract \(\mathbb F_2\)-curves because their canonical plane models lie in different projective orbits.

## Assumptions and scope

The base field is exactly \(\mathbb F_2\). The plane quartics are homogeneous ternary forms of degree four whose projective zero-loci are smooth over an algebraic closure. Isomorphism means over the ground field; every smooth plane quartic is its canonically embedded nonhyperelliptic genus-three curve, hence abstract isomorphism coincides with projective equivalence here.

Encode an equation by the integer mask \(m=\sum_i c_i2^i\), where \(i\) runs through monomials \(X^aY^bZ^{4-a-b}\) with \(a=0,\ldots,4\), then \(b=0,\ldots,4-a\). Coefficients \(c_i\in\mathbb F_2\). The four distinguishing mask equations are:

- 4249: \(Z^4+Y^3Z+Y^4+XY^2Z+X^3Z=0\).
- 4469: \(Z^4+Y^2Z^2+Y^4+XZ^3+XYZ^2+XY^3+X^3Z=0\).
- 4347: \(Z^4+YZ^3+Y^3Z+Y^4+XZ^3+XYZ^2+XY^2Z+X^3Z=0\).
- 4415: \(Z^4+YZ^3+Y^2Z^2+Y^3Z+Y^4+XZ^3+XY^3+X^3Z=0\).

## Proof

**Exhaustive orbit reduction.** There are exactly \(2^{15}-1=32767\) nonzero quartic forms. The three invertible coordinate substitutions (swap, elementary shear and cyclic permutation) generate the full \(168\)-element group \(\mathrm{GL}_3(\mathbb F_2)\). Breadth-first orbit generation produces \(279\) nonzero projective orbits. In each, geometric smoothness is equivalent to the absence of a common zero of the quartic and all first partials on the three affine patches \(X=1\), \(Y=1\), \(Z=1\) over an algebraic closure. Gröbner bases over \(\mathbb F_2\) decide these three ideal-unit tests exactly. Exactly \(78\) smooth orbits remain, of combined size \(10920\).

**Zeta numerators.** For each orbit representative, direct projective point counts over \(\mathbb F_{2^n}\) for \(n=1,2,3\) give \(N_n\). Put \(S_n=2^n+1-N_n\). Newton identities give \(a_1=-S_1\), \(2a_2=S_1^2-S_2\), \(6a_3=-S_1^3+3S_1S_2-2S_3\). For a genus-three curve, the functional equation then gives \(P_C(T)=1+a_1T+a_2T^2+a_3T^3+2a_2T^4+4a_1T^5+8T^6\). The \(78\) triples \((a_1,a_2,a_3)\) have \(73\) distinct values and five two-element fibres.

**Contact splitting.** For each of the seven rational projective lines \(L\), a basis for its two-dimensional linear subspace is chosen and the restriction of the quartic to that line is written as a binary quartic. In characteristic two it is a square of a binary quadratic if and only if its coefficients on the odd mixed-power monomials vanish. The (uniquely determined) square-root binary quadratic is evaluated on the three rational points of \(\mathbb P^1(\mathbb F_2)\). It has either 0, 1, or 2 distinct rational roots, which are exactly the respective contact types 0, 1, 2. Exhausting the seven lines for all 78 representatives gives 75 distinct joint \((P_C,\theta)\) values. Comparing each of the five zeta-polynomial collision pairs shows different signatures exactly when \((a_1,a_2,a_3)=(-1,1,0)\) or \((0,0,3)\).

**Direct witnesses.** On mask 4249 the only bitangent is \(Z=0\), with restriction \(Y^4\), a rational hyperflex. On mask 4469 the only bitangent is \(X=0\), with restriction \((Y^2+YZ+Z^2)^2\); its contact quadratic is irreducible over \(\mathbb F_2\). On mask 4347 the only bitangent is \(Z=0\), restriction \(Y^4\). On mask 4415 the only bitangent is \(X+Y=0\), with restriction \((Z^2+YZ)^2\), giving two distinct rational contacts. Each pair has identical point counts through degree three and hence identical full Weil polynomial. All four representatives pass the three-patch geometric smoothness tests and lie in distinct projective orbits.

## Verification

Execute `python verify_census.py` (Python 3 with SymPy). It checks the 168 group elements, all 32767 nonzero forms via 279 group orbits, all three geometric smoothness patch ideals, all 78 zeta numerators, all seven line restrictions and the two distinguishing pairs; it recreates `quartic_joint_census.csv`. Its observed terminal assertion was `CENSUS_OK 279 78 10920 73 75`.

Execute `python verify_independent.py` after the census. This independently implements finite-field multiplication and all 546 line-restriction computations, independently counts points over fields of degrees one through three for every representative, and checks degrees four through six for all four distinguishing examples. Its observed assertion was `INDEPENDENT_OK 78 full_profiles 546 extended_examples 4`. The bundled CSV records every representative's orbit size, first three point counts, Weil coefficients and contact signature. Exact arithmetic is used throughout; the claim is a finite exhaustive theorem, not an extrapolation from a sample.

## Relationship to prior work

Sutherland and Voloch (2017, Example 4.4) investigate arithmetic invariants finer than point-counting and discuss a pair of smooth quartic curves over \(\mathbb F_2\) that share Weil and certain cover zeta polynomials. Their motivation supports distinguishing isogeny-equivalent curves by geometric arithmetic data; the specific joint classification and the two contact-splitting distinctions above are separate claims. Costa, Harvey and Sutherland (2022) develop point-counting methods for smooth plane quartics; their algorithms do not by themselves imply this joint theta-contact classification. A previously available enumeration of geometric bitangent Frobenius orbit profiles and marginal contact signatures is not claimed as new. The novelty asserted here is the joint matching of zeta polynomials to rational contact divisor splitting, with explicit equal-zeta counterexamples.

## Limitations

The statement concerns characteristic two over the prime field, smooth genus-three plane quartics only; it makes no claim for larger finite fields. It does not assert that the individual zeta distribution, bitangent enumeration, or number of smooth quartics is novel. A pre-existing unindexed joint table might cover these exact pairs. External independent audit has not been performed.

## References

1. A. V. Sutherland and J. F. Voloch, *Maps between curves and arithmetic obstructions*, 2017, arXiv:1709.05734, Example 4.4. Freely accessible author manuscript: https://math.mit.edu/~drew/conm14532.pdf.
2. E. Costa, D. Harvey and A. V. Sutherland, *Counting points on smooth plane quartics*, 2022, arXiv:2208.09890, published in Research in Number Theory (2022). https://doi.org/10.1007/s40993-022-00397-8.
