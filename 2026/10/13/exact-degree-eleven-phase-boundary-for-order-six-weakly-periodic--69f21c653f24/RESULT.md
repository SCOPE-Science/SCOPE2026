# Exact degree-eleven phase boundary for order-six weakly periodic Ising states

## Finding

For the order-six Cayley-tree Ising model with \(|A|=k=6\) on the invariant set \(I_3\) studied by Ganikhodjaev, Rahmatullaev, and Rodzhan, the critical parameter denoted \(\alpha_c\) in their Theorem 4 is exactly algebraic. It is the unique real root in \((1.894515,1.894516)\) of
\[
P(\alpha)=256\alpha^{11}+384\alpha^{10}+160\alpha^9-2817\alpha^8-4996\alpha^7+3278\alpha^6+3680\alpha^5+7579\alpha^4+2880\alpha^3-4032\alpha^2-6912.
\]
The polynomial \(P\) is irreducible over \(\mathbb Q\). Consequently \(\alpha_c\) has algebraic degree exactly \(11\), and numerically
\[
\alpha_c=1.89451559917797127449\ldots.
\]

Equivalently, let \(\xi_c\) be the unique real root greater than \(2\) of
\[
J(\xi)=4\xi^{11}-26\xi^9-25\xi^8+62\xi^7+120\xi^6-60\xi^5-174\xi^4+30\xi^3+72\xi^2-18\xi-9.
\]
Then
\[
2.07717459<\xi_c<2.07717460,
\qquad
\alpha_c=\frac{5\xi_c^4-12\xi_c^2+3}{4\xi_c^3-6\xi_c}.
\]
Replacing the decimal threshold in the source theorem by this exact number gives its phase partition without changing the source's count: in the stated \(I_3\) regime there are no nonperiodic \(H_A\)-weakly periodic Gibbs measures below \(\alpha_c\), two at \(\alpha_c\) and on \([2,3]\), and four on \((\alpha_c,2)\cup(3,\infty)\).

## Assumptions and scope

The object is exactly the nearest-neighbor Ising model and weak-periodicity construction of arXiv:1707.01479v1, with Cayley-tree order \(k=6\), \(|A|=k\), invariant set \(I_3\), and the source parameter \(\alpha\). The result identifies the critical constant already defined by the source; it does not alter the source's boundary-law-to-Gibbs-measure correspondence or assert anything about weakly periodic states outside \(I_3\).

The source reduces nontrivial positive solutions by \(\xi=u+u^{-1}>2\) to
\[
G(\xi,\alpha)=\xi^5-\alpha\xi^4-4\xi^3+3\alpha\xi^2+3\xi+\alpha^2-\alpha=0
\]
and defines \(\alpha_c\) as the minimum of its lower \(\alpha\)-branch. It gives only \(\xi_0\approx2.077\) and \(\alpha_c\approx1.89\).

## Proof

At an interior minimum of the lower branch, differentiating \(G(\xi,\alpha(\xi))=0\) gives \(G_\xi=0\). Here
\[
G_\xi=5\xi^4-4\alpha\xi^3-12\xi^2+6\alpha\xi+3,
\]
so for \(\xi>2\),
\[
\alpha=A(\xi):=\frac{5\xi^4-12\xi^2+3}{4\xi^3-6\xi}.
\]
Direct exact substitution gives
\[
G(\xi,A(\xi))=-\frac{J(\xi)}{4\xi^2(2\xi^2-3)^2}.
\]
An exact Sturm sequence for \(J\) has one and only one zero on \((2,\infty)\), and it has exactly one zero in \((2.07717459,2.07717460)\). Call it \(\xi_c\).

The derivative
\[
A'(\xi)=\frac{10\xi^6-21\xi^4+18\xi^2+9}{2\xi^2(2\xi^2-3)^2}
\]
is positive for \(\xi>2\): with \(y=\xi^2\ge4\), the numerator is \(10y^3-21y^2+18y+9\), which is positive at \(y=4\), while its derivative \(30y^2-42y+18\) has negative discriminant and positive leading coefficient. Exact rational evaluation at the two endpoints of the isolating interval yields
\[
1.894515<A(2.07717459)<A(\xi_c)<A(2.07717460)<1.894516.
\]
At \(\xi=2\) the lower branch has value \(2\), whereas the displayed critical value is strictly smaller; together with the source's divergent endpoint behavior, the unique stationary point on \((2,\infty)\) is the unique global minimum defining \(\alpha_c\).

Eliminating \(\xi\) from \(G=0\) and \(G_\xi=0\) gives
\[
\operatorname{Res}_{\xi}(G,G_\xi)=-P(\alpha).
\]
Equivalently, after substituting \(\alpha=A(\xi)\), exact polynomial division shows that the numerator of \(P(A(\xi))\) is divisible by \(J(\xi)\). Hence \(P(\alpha_c)=0\). A Sturm sequence for \(P\) gives exactly one root in \((1.894515,1.894516)\), identifying the relevant resultant root without ambiguity.

Finally, \(P\) is primitive. Its reduction modulo \(41\) is irreducible: since \(\deg P=11\) is prime, the exact Rabin test reduces to
\[
\gcd(P,X^{41}-X)=1,
\qquad
X^{41^{11}}-X\equiv0\pmod{P,41}.
\]
Both identities are checked by finite-field polynomial arithmetic in the accompanying verifier. Gauss's lemma therefore makes \(P\) irreducible over \(\mathbb Q\), proving that \(\alpha_c\) has degree \(11\).

## Verification

The standalone verifier uses exact rational arithmetic to reconstruct the substitution identity, perform Sturm root counts for \(J\) on \((2,\infty)\) and in the tight isolating interval, perform a Sturm count for \(P\) in \((1.894515,1.894516)\), verify the elimination divisibility, and execute the irreducibility test modulo \(41\). Its successful output is

`VERIFY_OK J_gt2=1 J_tight=1 P_tight=1 elimination=exact irreducible_mod41=1`

The numerical decimal is descriptive; no finite floating-point experiment is used to establish uniqueness, algebraicity, or irreducibility.

## Relationship to prior work

The primary paper derives the same scalar equation \(G(\xi,\alpha)=0\), writes the two radical branches, and states that the lower branch has a unique minimum at \(\xi_0\approx2.077\) with \(\alpha_c\approx1.89\). It then uses that decimal-defined threshold in Theorem 4 to count the weakly periodic Gibbs measures. It does not give \(J\), \(P\), an isolating interval for \(\alpha_c\), or its algebraic degree.

The earlier weak-periodic Ising literature cited by the source treats smaller tree orders; the primary paper itself states that its predecessor analysis covered \(k<5\). Later weak-periodic \(p\)-adic Potts work concerns a different state space, field, model, and tree order and does not imply this real Ising phase boundary. Targeted published-record searches under the source identifier, order-six aliases, the decimal threshold, the exact polynomial structure, and algebraic-critical-value language did not return a covering result.

## Limitations

The result exactifies the critical constant and its algebraic structure for the source's \(k=6\), \(|A|=k\), \(I_3\) branch. It does not reclassify all weakly periodic measures outside \(I_3\), does not address extremality or thermodynamic dominance, and does not supply analogous exact critical polynomials for other tree orders. The measure counts quoted above are those already proved by the primary source; the new claim is the exact identification of their order-six boundary.

## References

1. N. Ganikhodjaev, M. Rahmatullaev, and M. H. Bin Mohd Rodzhan, *Weakly periodic Gibbs measures of the Ising model on the Cayley tree of order five and six*, arXiv:1707.01479v1; DOI:10.1007/s11040-017-9260-2. First public version: 2017-07-05. Primary Mathematics Subject Classification: 82B20.
2. U. A. Rozikov and M. M. Rakhmatullaev, *Description of weakly periodic Gibbs measures for the Ising model on a Cayley tree*, Theoretical and Mathematical Physics 156 (2008), DOI:10.1007/s11232-008-0091-y.
3. M. Rahmatullaev, A. Tukhtabaev, and N. Samijonova, *Weakly periodic p-adic quasi-Gibbs measures for the Potts model on a Cayley tree*, Letters in Mathematical Physics 114 (2024), article 129.
