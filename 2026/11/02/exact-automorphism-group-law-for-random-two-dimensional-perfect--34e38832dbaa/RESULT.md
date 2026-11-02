# Exact automorphism-group law for random two-dimensional perfect evolution algebras

## Finding
For every finite field \(K=\mathbb F_q\) of characteristic \(p\), select an invertible matrix \(M=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) uniformly from \(\operatorname{GL}_2(K)\) and define the evolution algebra \(E_M\) by \(e_1^2=ae_1+be_2\), \(e_2^2=ce_1+de_2\), and \(e_1e_2=0\). Write \(h=\gcd(2,q-1)\), \(g=\gcd(3,q-1)\), \(s=(q-1)^2\), and \(T=q(q-1)^2(q+1)\). The automorphism groups and their exact numbers of labelled structure matrices are:

\[
\begin{array}{c|cc}
 &g=1&g=3\\\hline
\operatorname{Aut}(E_M)=1&T-s(q+1-h)&T-s(q+1-h)\\
\operatorname{Aut}(E_M)\cong C_2&s(q+1-h)&s(q-h)\\
\operatorname{Aut}(E_M)\cong C_3&0&2s/3\\
\operatorname{Aut}(E_M)\cong S_3&0&s/3
\end{array}
\]

In particular,
\[
\Pr(\operatorname{Aut}(E_M)\ne 1)
 =\frac{q+1-h}{q(q+1)}
 =\begin{cases}1/(q+1),&q\text{ even},\\(q-1)/(q(q+1)),&q\text{ odd}.
 \end{cases}
\]
The result includes every finite field, including \(q=2\). The probability of rigidity tends to one with increasing field size, while the possibility of \(C_3\) or \(S_3\) depends exactly on the existence of nontrivial cube roots of unity in \(K\).

The algebra is simple exactly when \(bc\ne0\). Among the \(s(q^2-q+1)\) labelled simple algebras, precisely \(s(q-h)\) have nontrivial automorphism group. Thus
\[
\Pr(\operatorname{Aut}(E_M)\ne1\mid E_M\text{ simple})
 =\frac{q-h}{q^2-q+1}.
\]

## Assumptions and scope
All automorphisms are \(K\)-linear algebra automorphisms, not semilinear Galois automorphisms. Each invertible structure matrix relative to a fixed ordered natural basis is equally likely; the distribution is not uniform on algebra isomorphism classes. Two groups are identified up to abstract group isomorphism. The count is of field-rational automorphisms, not geometric automorphisms or scheme-theoretic infinitesimal points. Every result holds for every prime power \(q\ge2\). The perfection assumption is equivalent to \(ad-bc\ne0\).

## Proof
**1. Monomiality.** Let \(F\) be a \(K\)-linear automorphism. Because \(e_1e_2=0\), we have \(F(e_1)F(e_2)=0\). The vectors \(e_1^2,e_2^2\) form a basis by perfection, so if \(F(e_1)=x_1e_1+x_2e_2\) and \(F(e_2)=y_1e_1+y_2e_2\), then \(x_1y_1=x_2y_2=0\). Invertibility implies either \(F(e_1)=ue_1,F(e_2)=ve_2\), or \(F(e_1)=ue_2,F(e_2)=ve_1\), with \(u,v\in K^\times\). Conversely, preserving both basis squares for either such map suffices to preserve all products.

**2. Equations.** In the diagonal case the equations are
\[
au=au^2,\quad bv=bu^2,\quad cu=cv^2,\quad dv=dv^2.
\]
In the swapped case the equations are
\[
bv=cu^2,\quad au=du^2,\quad dv=av^2,\quad cu=bv^2.
\]
These identities follow by applying \(F\) to \(e_1^2\) and \(e_2^2\). They apply without any characteristic restriction.

**3. The support stratification.** Since \(ad-bc\ne0\), a matrix with exactly two nonzero entries is necessarily diagonal (\(a,d\ne0\)) or antidiagonal (\(b,c\ne0\)). A matrix with three nonzero entries has only the identity automorphism: the diagonal equations force both scalars to be one, and the swapped equations would exchange incompatible zero patterns. The all-nonzero and two-nonzero cases require separate analysis.

For all four entries nonzero, the diagonal equations give \(u=v=1\). The swapped equations give uniquely \(u=a/d\), \(v=d/a\), and the remaining condition is
\[
a^3c=bd^3.
\]
This nonidentity automorphism is an involution. Fix \(a,d\ne0\), and parameterize \(b=t a^2/d\) and \(c=t d^2/a\), where \(t\ne0\). The determinant is \(ad(1-t^2)\), hence the matrix is invertible precisely when \(t^2\ne1\). Since \(K^\times\) has exactly \(h\) solutions of \(t^2=1\), the all-nonzero matrices with automorphism group \(C_2\) number \(s(q-1-h)\).

For diagonal support, \(a,d\ne0\), \(b=c=0\). Besides the identity, the swapped map with \(u=a/d\) and \(v=d/a\) is the unique nonidentity automorphism. Thus all \(s\) such matrices have group \(C_2\).

For antidiagonal support, \(a=d=0\), \(b,c\ne0\). A diagonal automorphism is uniquely specified by \(u^3=1\) and \(v=u^2\), giving the cyclic group \(C_g\) where \(g=\gcd(3,q-1)\). A swapped map exists exactly when the equation \(u^3=b/c\) is soluble, and then there are exactly \(g\) swapped maps. If \(g=1\), there is one swapped map in every antidiagonal matrix and its group is \(C_2\). If \(g=3\), exactly \(s/3\) antidiagonal matrices admit a swapped map (each ratio \(b/c\) must be a cube), and their group is \(C_3\rtimes C_2\cong S_3\), the swapped map inverting diagonal scalars; the remaining \(2s/3\) matrices have group \(C_3\).

Combining the mutually exclusive strata yields the exact four group-order frequencies. The number of invertible \(2\)-by-\(2\) matrices is \(T=q(q-1)^2(q+1)\). Subtraction from \(T\) gives the identity-group count and division gives the probability formula.

**4. Simplicity.** If \(bc\ne0\), the natural-basis directed graph has both arrows, so it is strongly connected. Perfection then makes \(E_M\) simple: any nonzero ideal contains some nonzero \(e_i^2\), which propagates under multiplication to both basis squares, hence all of \(E_M\). Conversely, if \(b=0\) or \(c=0\), the span of the corresponding basis vector is a nonzero proper ideal. For each \((b,c)\in(K^\times)^2\), the determinant condition \(ad\ne bc\) permits exactly \(q^2-(q-1)=q^2-q+1\) choices of \((a,d)\). Thus the simple sample has size \(s(q^2-q+1)\). Among it, the nontrivial-automorphism matrices are exactly the \(s(q-1-h)\) all-nonzero symmetric cases plus the \(s\) antidiagonal cases; their sum is \(s(q-h)\). This yields the conditional probability formula.

## Verification
The accompanying dependency-free `verify.py` performs complete direct enumeration of invertible structure matrices and candidate monomial automorphisms over \(\mathbb F_q\) for \(q\in\{2,3,4,5,7,8,9,11,13,16\}\). It constructs extension-field multiplication from irreducible polynomials, checks each map against the actual multiplication equations, compares the full group-size histogram with the theorem, verifies the simple-algebra subpopulation, and reproduces the known number of two-dimensional perfect-algebra isomorphism classes by Burnside's lemma. Its successful completion prints `VERIFY_OK`. The field-by-field tests are not a proof for arbitrary \(q\); the symbolic support-stratification argument proves the general result.

## Relationship to prior work
The October 2026 evolution-algebra survey by Kaygorodov, Martín González and Viruel describes automorphism groups and identifies automorphism-order behavior over finite fields as a natural problem. The 2023 work of Cabrera Casado, Martín Barquero and Martín González classifies perfect two-dimensional evolution algebras via moduli, and Wei and Zou's 2023 paper gives their finite-field isomorphism-class counts. The 2024 study of two-dimensional automorphism group schemes by Cabrera Casado and collaborators describes possible automorphism-group structures. These results provide classification and group-theoretic machinery, but their inspected theorems and tables do not enumerate the *uniformly labelled invertible structure matrices by their abstract field-rational automorphism groups* or give the displayed exact rigidity probabilities. Indeed, summing the new counts weighted by automorphism-group order, and dividing by the monomial change-of-basis group size \(2(q-1)^2\), recovers Wei and Zou's previously known isomorphism-class counts, an independent consistency check; it does not reverse-infer the new distribution from a class count.

## Limitations
This is a finite-field dimension-two theorem, not a general-dimensional solution of automorphism-group classification or growth problems. It concerns labelled invertible structure matrices, not randomly chosen isomorphism classes, nonperfect algebras, scheme-theoretic automorphisms, or semilinear symmetries. Historical priority could be affected by classifications or finite-group-action tables not located or not fully accessible, especially under stabilizer-distribution terminology. 
## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, October 15, 2026; https://arxiv.org/html/2610.22248v1.
2. J. Wei, Y. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, 2023; https://arxiv.org/pdf/2310.12368.
3. Y. Cabrera Casado, D. Martín Barquero, C. Martín González, *Two-dimensional perfect evolution algebras over domains*, Journal of Algebraic Combinatorics 58 (2023), 569–587; https://doi.org/10.1007/s10801-022-01196-1.
4. Y. Cabrera Casado et al., *Hopf algebras and associative representations of two-dimensional evolution algebras*, arXiv:2407.15769v1, July 22, 2024; https://arxiv.org/abs/2407.15769.
