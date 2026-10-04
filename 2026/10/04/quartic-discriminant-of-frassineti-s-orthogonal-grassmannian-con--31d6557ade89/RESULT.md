# Quartic discriminant of Frassineti's orthogonal-Grassmannian conic bundle
## Finding
Let \(Y\) be a general fourfold in Frassineti's family \([\operatorname{OGr}(3,8),\mathcal S_-^{\otimes 2}\oplus\mathcal S_-\oplus\mathcal S_+^{\oplus 3}]\), and let \(\pi:Y\to Q^3\) be the conic bundle obtained from the first orthogonal-Grassmannian projection. Its scheme-theoretic discriminant \(\Delta_\pi\subset Q^3\) is an effective Cartier divisor in \(|\mathcal O_{Q^3}(4)|\). Thus, under \(Q^3\subset\mathbf P^4\), \(\Delta_\pi\) is a scheme-theoretic complete intersection of type \((2,4)\). In particular, \(\Delta_\pi\) is connected and Gorenstein with \(\omega_{\Delta_\pi}\cong\mathcal O_{\Delta_\pi}(1)\), \(K_{\Delta_\pi}^2=8\), \(h^1(\mathcal O_{\Delta_\pi})=0\), \(h^0(\omega_{\Delta_\pi})=5\), and \(\chi(\mathcal O_{\Delta_\pi})=6\). No smoothness, normality, or irreducibility assertion is made for the discriminant.

## Assumptions and scope
Work over \(\mathbf C\). Frassineti's Section 6 considers a general zero locus \(Y\) of \(\mathcal S_-^{\otimes2}\oplus\mathcal S_-\oplus\mathcal S_+^{\oplus3}\) on \(\operatorname{OGr}(3,8)\) and identifies the first projection as a conic bundle \(\pi:Y\to Q^3\). The discriminant is scheme-theoretic. No singularity type is assumed.

## Proof
Let \(p_+:\operatorname{OGr}(3,8)\to Q^6_+\) and \(p_-:\operatorname{OGr}(3,8)\to Q^6_-\) be the two \(\mathbf P^3\)-bundle projections. Hara gives
\[
p_+^*\mathcal O_{Q^6_+}(1)\cong\mathcal O_{p_-}(1),\qquad p_-^*\mathcal O_{Q^6_-}(1)\cong\mathcal O_{p_+}(1).
\]
The three \(\mathcal S_+\)-sections cut the base \(Q^6_+\) to a smooth \(Q^3\), while \(\mathcal S_-\) is the relative hyperplane bundle for \(p_+\). A general relative hyperplane corresponds to
\[
0\to\mathcal O_{Q^3}\to\mathcal S_+(1)|_{Q^3}\to F\to0
\]
with \(F\) locally free of rank three and hyperplane divisor \(\mathbf P_{Q^3}(F)\). For the rank-four spinor bundle on \(Q^6\), \(\det\mathcal S_+\cong\mathcal O(-2)\), hence
\[
\det F\cong\det(\mathcal S_+(1))|_{Q^3}\cong\mathcal O_{Q^3}(2).
\]
The remaining \(\mathcal S_-^{\otimes2}\)-section is a quadratic equation on \(\mathbf P_{Q^3}(F)\), equivalently a symmetric map \(F^\vee\to F\). Its determinant is a section of \((\det F)^{\otimes2}\cong\mathcal O_{Q^3}(4)\). Its zero scheme is the conic discriminant. Since \(Y\) is smooth over characteristic zero, the conic bundle is generically smooth, so the determinant is nonzero and defines an effective Cartier divisor \(\Delta_\pi\in|4H|\).

Since \(Q^3\subset\mathbf P^4\) is a quadric and sections of \(\mathcal O_{Q^3}(4)\) lift to quartics on \(\mathbf P^4\), \(\Delta_\pi\) is a scheme-theoretic complete intersection of degrees \(2\) and \(4\). Adjunction gives \(\omega_{\Delta_\pi}\cong\mathcal O_{\Delta_\pi}(1)\). As \(H^3=2\) on \(Q^3\), \(K_{\Delta_\pi}^2=4H^3=8\). From
\[
0\to\mathcal O_{Q^3}(-4)\to\mathcal O_{Q^3}\to\mathcal O_{\Delta_\pi}\to0
\]
and Serre duality, the only nonzero higher cohomology of \(\mathcal O_{Q^3}(-4)\) is \(H^3\cong H^0(\mathcal O_{Q^3}(1))^\vee\cong\mathbf C^5\). Thus \(h^0(\mathcal O_{\Delta_\pi})=1\), \(h^1=0\), \(h^2=5\), and hence \(h^0(\omega)=5\) and \(\chi=6\).

## Verification
The bundled verifier checks the determinant exponents, adjunction arithmetic, and the complete-intersection Hilbert-polynomial value \(\chi=6\); it prints `VERIFY_OK`. The nonstandard geometric inputs are sourced in the references.

## Relationship to prior work
Frassineti states the model and conic bundle but not this discriminant class in the inspected Section 6 passage. Hara supplies the \(D_4\)-roof geometry, while Tanaka supplies scheme-theoretic conic-discriminant foundations. Bernardara--Fatighenti--Manivel--Tanturri compute a quartic discriminant for a different conic-bundle Fano fourfold over \(Q^3\), with \((-K)^4=114\) and \(h^0(-K)=30\); Frassineti's family has inspected invariants \((-K)^4=100\), \(h^0(-K)=27\), and \(\chi(T)=-20\), so that result does not imply the present fixed-family statement.

## Limitations
No claim is made about the singular locus, reducedness, normality, irreducibility, or birational type of \(\Delta_\pi\). Originality remains subject to unindexed or differently phrased literature.

## References
1. Alessandro Frassineti, *Prime Fano fourfolds in classical and generalized Grassmannians*, arXiv:2609.09310v1, Section 6.
2. Wahei Hara, *Derived equivalence for the simple flop of type \(G_2^\dagger\) via tilting bundles*, arXiv:2412.14314v3, Section 2.1.
3. A. G. Kuznetsov and Yu. G. Prokhorov, *1-nodal Fano threefolds with Picard number 1*, DOI 10.4213/im9585e, Proposition C.5.
4. Hiromu Tanaka, *Discriminant Divisors for Conic Bundles*, DOI 10.1093/qmath/haae046.
5. Marcello Bernardara, Enrico Fatighenti, Laurent Manivel, and Fabio Tanturri, *Fano fourfolds of K3 type*, DOI 10.5802/aif.3761, p. 43.
