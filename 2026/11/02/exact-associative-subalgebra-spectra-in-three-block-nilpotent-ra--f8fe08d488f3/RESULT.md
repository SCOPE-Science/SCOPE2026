# Exact associative-subalgebra spectra in three-block nilpotent radicals

## Finding
For any prime power \(q\) and integer \(r\geq 1\), let \(A_r(\mathbb F_q)\) be the nonunital associative algebra of strictly upper three-block matrices, with diagonal block sizes \((1,r,1)\) and zero diagonal blocks. Write its elements as
\[
 X(u,v,c)=\begin{pmatrix}0&u&c\\0&0&v\\0&0&0\end{pmatrix},
 \qquad u\in\mathbb F_q^{1\times r},\quad v\in\mathbb F_q^{r\times1},\quad c\in\mathbb F_q.
\]
Multiplication is \(X(u,v,c)X(u',v',c')=X(0,0,uv')\). The square \(A_r^2=kz\) is the one-dimensional two-sided annihilator, where \(z=X(0,0,1)\).

Let \(N_{r,d}(q)\) count the \(d\)-dimensional \(\mathbb F_q\)-linear associative subalgebras, including the zero subalgebra. Set \(\genfrac{[}{]}{0pt}{}{n}{j}_q\) to be the Gaussian binomial coefficient, zero outside \(0\leq j\leq n\), and set \(G_t(q)=\lvert\mathrm{GL}_t(\mathbb F_q)\rvert=\prod_{i=0}^{t-1}(q^t-q^i)\), with \(G_0(q)=1\). Then for \(0\leq d\leq 2r+1\),
\[
\boxed{N_{r,d}(q)=\genfrac{[}{]}{0pt}{}{2r}{d-1}_q +q^d\!\!\sum_{\substack{0\le a\le r,\ 0\le b\le r-a,\\0\le t\le\min(a,b),\ a+b-t=d}}
\genfrac{[}{]}{0pt}{}{r}{a}_q\genfrac{[}{]}{0pt}{}{r-a}{b}_q
\genfrac{[}{]}{0pt}{}{a}{t}_q\genfrac{[}{]}{0pt}{}{b}{t}_qG_t(q).}
\]
The second summand is exactly the number of subalgebras not containing \(A_r^2\). Every such subalgebra has zero multiplication and dimension at most \(r\); hence for \(d>r\), \(N_{r,d}(q)=\genfrac{[}{]}{0pt}{}{2r}{d-1}_q\). This cutoff is sharp: exactly
\[
\boxed{q^r\sum_{a=0}^r\genfrac{[}{]}{0pt}{}{r}{a}_q}
\]
subalgebras of the largest possible dimension \(r\) avoid \(A_r^2\).

## Assumptions and scope
The field is an arbitrary finite field, not necessarily of prime cardinality. The block-radical multiplication has no identity, and subalgebra means a vector subspace closed under that multiplication; no requirement to contain an identity is imposed. The integer \(r\) is unrestricted and at least one. Empty sums have value zero. The formula is a count of distinct subspaces, not of embeddings, generators, or conjugacy classes. The result makes no statement about subalgebras of the corresponding full unital parabolic matrix algebra.

## Proof
Put \(U=k^{1\times r}\), \(V=k^{r\times1}\), \(W=U\oplus V\) and \(Z=kz\), so \(A_r=W\oplus Z\). Associativity is immediate from \(A_r^2\subseteq Z\) and \(ZA_r=A_rZ=0\). The pairing \(U\times V\to k\), \((u,v)\mapsto uv\), is nondegenerate, and \(A_r^2=Z\).

**Central-containing case.** If a vector subspace \(H\) contains \(Z\), then every product of its elements belongs to \(Z\subseteq H\). Thus every such subspace is an associative subalgebra. Quotienting by \(Z\) identifies \(d\)-dimensional such subspaces with \((d-1)\)-dimensional subspaces of \(W\); their number is \(\genfrac{[}{]}{0pt}{}{2r}{d-1}_q\).

**Central-avoiding case.** If \(H\cap Z=0\), then any product of two elements of \(H\) lies in both \(H\) and \(Z\), so \(H\) is a subalgebra if and only if its multiplication is identically zero. Projection \(A_r\to W\) maps \(H\) isomorphically onto a \(d\)-space \(S\le W\); conversely, each such \(S\) has exactly \(q^d\) graph lifts \(\{s+\ell(s)z:s\in S\}\), one for each \(\ell\in S^*\). All graph lifts are subalgebras precisely when \(uv'=0\) for every \((u,v),(u',v')\in S\).

Let \(U_0=\pi_U(S)\), \(V_0=\pi_V(S)\), of dimensions \(a\) and \(b\). The last vanishing condition is equivalent to \(U_0\perp V_0\) under the natural pairing. There are \(\genfrac{[}{]}{0pt}{}{r}{a}_q\genfrac{[}{]}{0pt}{}{r-a}{b}_q\) choices of this ordered orthogonal pair: first choose \(U_0\), then a \(b\)-space of its annihilator in \(V\), which has dimension \(r-a\). In particular \(a+b\le r\).

For fixed \((U_0,V_0)\), the subspaces \(S\le U_0\oplus V_0\) projecting surjectively to both factors are classified by the linear Goursat correspondence. Put \(K_U=\{u:(u,0)\in S\}\) and \(K_V=\{v:(0,v)\in S\}\). Then \(U_0/K_U\cong V_0/K_V\) via the relation \(S\). If the common quotient dimension is \(t\), there are \(\genfrac{[}{]}{0pt}{}{a}{t}_q\genfrac{[}{]}{0pt}{}{b}{t}_qG_t(q)\) such subspaces: choose the two kernels and an isomorphism between their quotients. The dimension of \(S\) is \(a+b-t\). Summing over exactly those \((a,b,t)\) with \(a+b-t=d\) and multiplying by the \(q^d\) graph choices gives the asserted second summand. The two cases are disjoint and exhaustive.

Since \(a+b\le r\) and \(t\ge0\), central-avoiding subalgebras satisfy \(d=a+b-t\le r\). Equality forces \(a+b=r\) and \(t=0\); then \(V_0=U_0^\perp\) and \(S=U_0\oplus V_0\). There are \(\sum_{a=0}^r\genfrac{[}{]}{0pt}{}{r}{a}_q\) such \(S\), each with \(q^r\) graph lifts. This proves the sharp cutoff and its count.

## Verification
The accompanying `CHECK.py` independently generates every reduced-row-echelon subspace of \(\mathbb F_q^{2r+1}\) for eight small field/rank configurations, checks closure of each basis under matrix multiplication, and compares the dimension census with the formula. The field of four elements is explicitly represented by \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\). The observed distributions are:

| \((r,q)\) | \((N_{r,0},\ldots,N_{r,2r+1})\) |
| --- | --- |
| \((1,2)\) | \((1,5,3,1)\) |
| \((1,3)\) | \((1,7,4,1)\) |
| \((1,4)\) | \((1,9,5,1)\) |
| \((1,5)\) | \((1,11,6,1)\) |
| \((2,2)\) | \((1,19,35,35,15,1)\) |
| \((2,3)\) | \((1,49,94,130,40,1)\) |
| \((2,4)\) | \((1,101,197,357,85,1)\) |
| \((3,2)\) | \((1,71,371,779,1395,651,63,1)\) |

Run `python3 CHECK.py` from the directory containing that file. The exact success marker is `GENERALIZED_HEISENBERG_SUBALGEBRA_OK`. These finite checks support, but do not replace, the counting proof.

## Relationship to prior work
The standard Heisenberg **Lie** algebra arises by taking commutators of the smallest block case, but Lie-subalgebra counts are not associative-subalgebra counts: every line is a Lie subalgebra, whereas in this nonunital associative algebra a line need not be closed under squaring. For example, over \(\mathbb F_2\), the associative algebra with \(r=1\) has ten subalgebras, while its Heisenberg Lie algebra has twelve. Previously developed Lie-ring subalgebra/ideal zeta functions thus do not, without an additional argument, imply the associative formula. Existing coclass studies describe or enumerate **isomorphism types of algebras**, not the subalgebra dimension spectrum of each algebra in this particular parabolic-radical family. The two enumeration problems have different objects and quantifiers.

The displayed result is derived directly from subspace projection geometry and the linear Goursat correspondence. The latter is an established method; no priority is claimed for Gaussian-binomial arithmetic or for the correspondence itself. The assessed contribution is the simultaneous uniform associative-subalgebra dimension census, structural cutoff, and maximal-disjoint count for this natural unbounded family. The consulted sources and remaining search limitations are detailed in `REVIEW.md` and `AUDIT.json`.

## Limitations
This theorem does not enumerate unital subalgebras of parabolic algebras, arbitrary class-two associative algebras, integral suborders, subalgebra isomorphism types, or automorphism orbits. It is a finite-field count, not a classification of schemes of subalgebras. Absence of an equivalent historical result has not been independently certified; some relevant papers could be inaccessible or unindexed.

## References
1. L. Woodward, *Zeta functions of Lie rings of upper-triangular matrices*, Journal of the London Mathematical Society 77 (2008), 69–82; first online 2007-11-22, DOI `10.1112/jlms/jdm068`. Distinct Lie-ring/ideal-zeta problem.
2. B. Eick and T. Moede, *Nilpotent associative algebras and coclass theory*, Journal of Algebra 434 (2015), 249–260, DOI `10.1016/j.jalgebra.2015.03.027`. Algebra isomorphism/coclass framework, not this subalgebra census.
3. T. Moede, *Coclass theory for nilpotent associative algebras*, doctoral thesis (2016), `https://d-nb.info/1175818445/34`. Accessible full text; sections on annihilators, split extensions, and coclass structure.
4. B. Eick and T. Moede, *Coclass Theory for Finite Nilpotent Associative Algebras: Algorithms and a Periodicity Conjecture*, Experimental Mathematics 26 (2017), 267–274; first online 2016-08-12, DOI `10.1080/10586458.2016.1162229`. Counting and classification context.
5. S. Rossmann, *Zeta — computing zeta functions of groups, algebras, and modules*, public documentation `https://www.maths.nuigalway.ie/~rossmann/Zeta/`. Heisenberg **Lie** subalgebra zeta example, over local rings rather than finite-field associative subalgebras.
