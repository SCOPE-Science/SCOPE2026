# Canonical-line rigidity throughout four ambient ample cones of Calabi–Yau fourfolds

## Finding

Let \(k\in\{0,1,2,3\}\). For the blowup \(Y_k=\operatorname{Bl}_{\mathbb P^k}\mathbb P^5_{\mathbb C}\), let \(H\) be the pullback hyperplane class and \(E\) the exceptional divisor. Every smooth anticanonical hypersurface \(Z\subset Y_k\) is a Calabi–Yau fourfold. For any integers \(a>b>0\), the ambient-induced polarization \(L=(aH-bE)|_Z\) is ample, and its Hilbert polynomial has **four distinct roots on the imaginary axis**.

More precisely, set \(u=a-b>0\) and write
\[
P_{k,a,b}(t)=\chi(Z,L^{\otimes t})=A_k(b,u)t^4+B_k(b,u)t^2+2.
\]
The exact coefficient pairs, with \(A_k>0\) and \(B_k>0\), are
\[
\begin{array}{c|l|l}
k&A_k(b,u)&B_k(b,u)\\ \hline
0&b^4/12+b^3u+3b^2u^2/2+bu^3+u^4/4&35b^2/12+15bu/2+15u^2/4\\
1&b^3u/2+3b^2u^2/2+bu^3+u^4/4&2b^2+7bu+15u^2/4\\
2&b^2u^2+bu^3+u^4/4&b^2+6bu+15u^2/4\\
3&5bu^3/6+u^4/4&25bu/6+15u^2/4
\end{array}
\]
Their quadratic discriminants \(\Delta_k=B_k^2-8A_k\) satisfy
\[
\begin{aligned}
144\Delta_0&=1129b^4+5148b^3u+9522b^2u^2+6948bu^3+1737u^4,\\
16\Delta_1&=64b^4+384b^3u+832b^2u^2+712bu^3+193u^4,\\
16\Delta_2&=16b^4+192b^3u+568b^2u^2+592bu^3+193u^4,\\
144\Delta_3&=u^2(2500b^2+3540bu+1737u^2).
\end{aligned}
\]
All expressions are strictly positive for \(b,u>0\). Consequently the roots of \(P_{k,a,b}\) are simple and purely imaginary. Equivalently, the Chern numbers satisfy the **strict inequality**
\[
\boxed{\bigl(c_2(Z)\cdot L^2\bigr)^2>192\,L^4.}
\]
This is uniform across the full open two-parameter ambient ample cone for each of the four blowup types.

## Assumptions and scope

The ground field is \(\mathbb C\); the center \(\mathbb P^k\subset\mathbb P^5\) is linear and \(0\le k\le3\). Its codimension is \(c=5-k\). On the blowup, \(-K_{Y_k}=6H-(c-1)E\), which is ample and globally generated since \(6>c-1>0\). Bertini provides smooth connected anticanonical members. Adjunction yields \(K_Z\cong\mathcal O_Z\). Standard cohomology of a Fano fivefold and its anticanonical divisor gives \(h^0(Z,\mathcal O_Z)=h^4(Z,\mathcal O_Z)=1\) and \(h^i(Z,\mathcal O_Z)=0\) for \(1\le i\le3\). Thus \(\chi(\mathcal O_Z)=2\). The strict inequalities concern exactly \(a>b>0\), so no assertion is made on the nef boundary or for ample line bundles not induced by \(Y_k\).

## Proof

**Step 1: Count ambient sections.** Define the polynomial \(\binom{x}{m}=x(x-1)\cdots(x-m+1)/m!\). For nonnegative integers \(s\ge r\), the dimension of the space of degree-\(s\) polynomials vanishing to order at least \(r\) on the linear center is
\[
C_k(s,r)=\binom{s+5}{5}-\sum_{j=0}^{r-1}\binom{j+c-1}{c-1}\binom{s-j+k}{k}.
\]
The summand counts monomials with total normal degree \(j\) and tangent degree \(s-j\); these are exactly the forbidden monomials for \(\mathcal O(sH-rE)\). Summation of a polynomial in \(j\) by Faulhaber's formula produces a polynomial extension of \(C_k(s,r)\) to all integer \(s,r\). For \(s\gg r\gg0\), higher cohomology vanishes, so this extension is the bivariate Euler-characteristic polynomial \(\chi(Y_k,\mathcal O(sH-rE))\), valid for all integers by Riemann–Roch.

**Step 2: Apply anticanonical subtraction.** The divisor exact sequence
\[
0\longrightarrow\mathcal O_{Y_k}(t(aH-bE)+K_{Y_k})\longrightarrow\mathcal O_{Y_k}(t(aH-bE))\longrightarrow L^{\otimes t}\longrightarrow0
\]
gives for every integer \(t\)
\[
P_{k,a,b}(t)=C_k(ta,tb)-C_k(ta-6,tb-(c-1)).
\]
Expanding the finite polynomial sums with rational arithmetic yields precisely the four \(A_k,B_k\) entries in the table above and constant term \(2\). Odd powers vanish, consistently with Serre duality on \(Z\). For reproduction, run `python3 artifacts/verify.py`, which independently constructs the binomial-sum polynomials, checks all four coefficient identities, checks all four discriminant factorizations, and compares with direct nonnegative monomial counts in admissible cases.

**Step 3: Root-location conclusion.** Since \(b>0\), \(u=a-b>0\), all the displayed coefficients of \(A_k\), \(B_k\) and \(\Delta_k\) are positive (zero coefficients omitted), and \(A_k,B_k,\Delta_k>0\). Writing \(z=t^2\), the two roots of \(A_k z^2+B_k z+2\) are real and distinct because \(\Delta_k>0\). Their sum \(-B_k/A_k\) and product \(2/A_k\) show that both roots are strictly negative. Thus the four square roots in \(t\) are nonzero, simple, and lie on the imaginary axis.

**Step 4: Characteristic-number restatement.** Hirzebruch–Riemann–Roch on a Calabi–Yau fourfold gives
\[
P_{k,a,b}(t)=\frac{L^4}{24}t^4+\frac{c_2(Z)\cdot L^2}{24}t^2+2.
\]
Hence \(\Delta_k=((c_2(Z)\cdot L^2)^2-192L^4)/576\). Strict positivity of the explicit discriminants proves the claimed Chern inequality.

## Verification

The independent symbolic polynomial calculation reconstructs \(C_k\) using finite Faulhaber summation for each \(k\in\{0,1,2,3\}\), verifies \(P_{k,a,b}\) coefficient by coefficient over \(\mathbb Q[a,b,t]\), and verifies the four exact identities for \(\Delta_k\) after substituting \(a=b+u\). Direct monomial-count evaluations in the region \(s\ge r\ge0\) provide a separate combinatorial cross-check. No finite test is used in place of the proof of strict positivity for all \(b,u>0\), which is an immediate consequence of the displayed positive-coefficient identities. The checker requires Python 3 and SymPy.

## Relationship to prior work

Weitsman's 2026 theorem identifies Hilbert polynomials of smooth anticanonical hypersurfaces in smooth toric varieties with lattice-point counts on polytope boundaries. That broad result already provides a general means of computing these polynomials; the binomial construction here is an elementary direct specialization for linear-center blowups and is not itself claimed as the new insight. The result established here is the **simultaneous, strict root-location and Chern-discriminant statement for every positive ambient polarization in four complete blowup families**. Golyshev's earlier canonical-strip transfer result concerns the anticanonical polarization on the Fano ambient space. Belmans–Galkin–Mukhopadhyay examine canonical-strip failures and establish background evidence about toric Fano examples, but their results inspected do not yield the claimed all-polarizations statement for the present families. No assertion of definitive historical priority is made.

## Limitations

The proof treats only smooth anticanonical hypersurfaces of \(\operatorname{Bl}_{\mathbb P^k}\mathbb P^5\) for \(0\le k\le3\), with ambient-induced ample classes \(aH-bE\). It does not classify all Calabi–Yau fourfolds satisfying the canonical-line property, address higher-dimensional toric blowups, or claim the result for every ample class intrinsic to the hypersurface. The discriminants tend toward a boundary degeneration in some cases; strictness is asserted only in the open ample region. Historical uniqueness and independent validation remain open.

## References

1. Jonathan Weitsman, *Hilbert Polynomials of Calabi Yau Hypersurfaces in Toric Varieties and Lattice Points in Polytope Boundaries*, arXiv:2601.02176, first posted January 5, 2026; Theorem 1 and Sections 1, 4–5.
2. V. Golyshev, *The Canonical Strip, I*, arXiv:0903.2076 (2009), canonical-strip transfer for anticanonical divisors.
3. Pieter Belmans, Sergey Galkin and Swarnava Mukhopadhyay, *Examples Violating Golyshev's Canonical Strip Hypotheses*, Experimental Mathematics **31** (2022), 233–237, doi:10.1080/10586458.2019.1602571; Section 1 and Proposition 4.
4. Standard inputs: Bertini, adjunction, Riemann–Roch, Kodaira vanishing and Serre duality.
