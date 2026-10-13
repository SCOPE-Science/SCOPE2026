# Complete nullity distribution for two-by-two finite-field Sylvester operators

## Finding

Let \(k=\mathbb F_q\), for an arbitrary prime power \(q\). For ordered \(A,B\in M_2(k)\), set \(L_{A,B}:M_2(k)\to M_2(k)\), \(L_{A,B}(X)=AX-XB\). Put
\[
N_j(q)=\#\{(A,B)\in M_2(k)^2:\dim_k\ker L_{A,B}=j\}.
\]
**The complete distribution**, for all \(q\ge2\), is
\[
\begin{aligned}
N_0(q)&=q^3(q-1)(q^4-2q^2+q+1),\\
N_1(q)&=q^2(q-1)(q+1)^2(q^2-2),\\
N_2(q)&=q(q-1)(q^4+q^3+4q^2+3q+1),\\
N_4(q)&=q.
\end{aligned}
\]
For all other integers \(j\), \(N_j(q)=0\). In particular **nullity three never occurs**, and the operator ranks are exactly \(4,3,2,0\) (each occurs for every \(q\ge2\)). The probability of unique solvability of \(AX-XB=C\) for *every* prescribed right-hand side \(C\), when \((A,B)\) is uniformly distributed, is
\[
\Pr(L_{A,B}\text{ invertible})=\frac{(q-1)(q^4-2q^2+q+1)}{q^5}.
\]
For each fixed pair of nullity \(j\), the equation \(AX-XB=C\) has precisely \(q^{4-j}\) attainable right-hand sides, each with exactly \(q^j\) solutions, and no solutions for the remaining right-hand sides.

## Assumptions and scope

All matrices are arbitrary (not assumed invertible, diagonalizable, or distinct), and the pairs are **ordered**. The field is an arbitrary finite field, not necessarily prime; no characteristic exclusion is made. The kernel dimension and rank are dimensions over the base field \(k\). Counts do not quotient by simultaneous similarity. The source literature provides the classical Sylvester solvability theory, whereas the result here is the full weighted nullity census over both input matrices.

## Proof

**Module reduction.** Regard \(k^2\) as a \(k[t]\)-module via the action of \(A\), and similarly via \(B\). An intertwiner \(X\) satisfies \(AX=XB\), so
\[
\ker L_{A,B}=\operatorname{Hom}_{k[t]}(k^2_B,k^2_A).
\]
For cyclic primary modules associated with monic irreducible polynomials \(f,g\), an elementary annihilator calculation gives
\[
\dim_k\operatorname{Hom}_{k[t]}(k[t]/(f^a),k[t]/(g^b))=
\begin{cases}\deg(f)\min(a,b),&f=g,\\0,&f\ne g.\end{cases}
\]
Indeed the image of the class of \(1\) must be annihilated by \(f^a\); if \(f=g\) there are exactly \(q^{\deg(f)\min(a,b)}\) choices, and coprime primary factors contribute none. Direct sums turn these dimensions into sums.

**Similarity types and class sizes.** Every \(2\times2\) matrix has exactly one of the following forms up to similarity. The number of classes of a type, and the cardinality of each class, are:

| Type | Number of classes | Elements in each class |
| --- | ---: | ---: |
| Scalar \(\lambda I\) | \(q\) | \(1\) |
| Nontrivial Jordan block \(J_2(\lambda)\) | \(q\) | \(J=q^2-1\) |
| Two distinct rational eigenvalues \(\{\lambda,\mu\}\) | \(\binom q2\) | \(S=q(q+1)\) |
| Irreducible quadratic companion | \((q^2-q)/2\) | \(I=q(q-1)\) |

For clarity, \(|\mathrm{GL}_2(k)|=q(q-1)^2(q+1)\). Dividing by the corresponding invertible centralizer sizes \(|\mathrm{GL}_2(k)|\), \(q(q-1)\), \((q-1)^2\), and \(q^2-1\) gives the four class sizes. There are exactly \((q^2-q)/2\) monic irreducible quadratics and \(\binom q2\) unordered pairs of distinct field elements.

**Intertwiner cases.** Apply the primary-module dimension rule to each ordered pair of types. Nullity \(4\) is possible only for identical scalar matrices, producing \(N_4=q\). Nullity \(1\) occurs exactly in the two ordered Jordan/split positions sharing the Jordan eigenvalue, or in ordered distinct split spectra that meet in exactly one eigenvalue. Their weighted counts are
\[
N_1=2q(q-1)JS+q(q-1)(q-2)S^2
=q^2(q-1)(q+1)^2(q^2-2).
\]
Nullity \(2\) occurs precisely in the following mutually disjoint cases: scalar versus Jordan at the same eigenvalue; scalar versus split spectrum containing that eigenvalue; two Jordan blocks at the same eigenvalue; the identical split spectrum; and the identical irreducible quadratic. Their contributions give
\[
\begin{aligned}
N_2&=2qJ+2q(q-1)S+qJ^2+\binom q2S^2+\frac{q^2-q}{2}I^2\\
&=q(q-1)(q^4+q^3+4q^2+3q+1).
\end{aligned}
\]
No remaining pair shares a compatible primary component, so all remaining pairs have nullity \(0\). There is no nullity \(3\): the preceding exhaustive cases realize only \(0,1,2,4\). Since the sample space has exactly \(q^8\) ordered pairs,
\[
N_0=q^8-N_1-N_2-N_4=q^3(q-1)(q^4-2q^2+q+1).
\]
Finally, a linear map on a four-dimensional \(k\)-space with nullity \(j\) has image cardinality \(q^{4-j}\) and each nonempty fiber has cardinality \(q^j\); this proves the claims about prescribed right-hand sides. All reasoning is valid in characteristic two, since \(AX-XB=0\) is the definition of a module intertwiner regardless of sign conventions. This completes the proof.

## Verification

The accompanying dependency-free program `verify.py` computes the \(4\times4\) matrix of \(L_{A,B}\), exhaustively evaluates its rank for every ordered pair in \(M_2(k)^2\), and compares all four class counts with the formulas. It checks the prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) and the nonprime field \(\mathbb F_4\), implemented by \(u^2+u+1=0\). Running `python3 verify.py` terminates in `VERIFY_OK`. Observed counts, in the order \((N_0,N_1,N_2,N_4)\), are \((88,72,94,2)\), \((3618,2016,924,3)\), \((43968,16800,4764,4)\), and \((290500,82800,17320,5)\), respectively. These finite tests are corroborative; the classification and proof above cover all prime powers.

## Relationship to prior work

The existence and uniqueness criterion for the Sylvester equation, in terms of relatively prime characteristic/minimal polynomials, is classical. Ran and Rodman (2010) describe ranges and low-rank perturbations of Sylvester operators for fixed matrices; Charkani and Bouarga (2015), Proposition 4.1 and Theorem 4.12, analyze solvability and give an explicit inverse under coprimality. Neither result, in the inspected text, enumerates the four nullity strata of uniformly varying pairs \((A,B)\) over all finite fields. Britnell and Wildon (2010) develop the finite-field matrix similarity-type and commuting-class framework; this supplies relevant canonical-form background but studies commuting representatives of similarity classes, not the distribution of \(\dim\operatorname{Hom}_{k[t]}(k^2_B,k^2_A)\) over ordered pairs. These relationships motivate, but do not themselves provide the closed census established here. The usual Jordan-form and rational-canonical classification ingredients are not claimed to be new.

## Limitations

The theorem concerns only matrices of size \(2\times2\); it does not assert formulas for larger sizes, nor that the distribution cannot be recovered indirectly from broad matrix-enumeration machinery. Literature searches are not proofs of first discovery, and an equivalent pre-existing tabulation under intertwiners, Kronecker differences, or resultants may exist. The exhaustive computations for four fields are not used as infinite proofs. No independent audit or independent validation has been performed.

## References

1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (public preprint, 6 January 2010); later *J. London Math. Soc.* 83 (2011), 470–492.
2. A. C. M. Ran and L. Rodman, *Ranges of Sylvester maps and a minimal rank problem*, *Electronic Journal of Linear Algebra* 20 (2010), 126–135, DOI: 10.13001/1081-3810.1363.
3. M. E. Charkani and S. Bouarga, *Polynomial Solution of Sylvester Matrix Equation*, *International Journal of Algebra* 9 (2015), 185–194, DOI: 10.12988/ija.2015.5311 (published 15 May 2015).
