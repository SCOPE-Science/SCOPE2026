# Exact \(\ell_1\) distortion and cut rigidity of unit-edge \(K_{3,n}\) metrics

## Finding

Let \(n\geq3\) be an integer. Let \(X_n\) be the vertex set of the unweighted complete bipartite graph \(K_{3,n}\), with three vertices in \(A\) and \(n\) vertices in \(B\). Give \(X_n\) its shortest-path metric \(d\), so distinct vertices in the same part have distance \(2\) and vertices in opposite parts have distance \(1\). Set \(k=\lfloor(n+1)/3\rfloor\). Then the optimal real \(\ell_1\)-embedding distortion is

\[
\boxed{c_{\ell_1}(X_n)=2-\frac{k(2n+1-3k)}{n(n-1)}.}
\]

Equivalently, writing \(D_n=c_{\ell_1}(X_n)\),

\[
D_n=\begin{cases}
\frac53-\frac{2}{3n},&n\equiv1\pmod3,\\
\frac53-\frac{2}{3(n-1)},&n\equiv0,2\pmod3.
\end{cases}
\]

In particular, \(D_3=4/3\), \(D_4=D_5=3/2\), \(D_6=23/15\), \(D_7=D_8=11/7\); the sequence has consecutive plateaus \(D_{3q+1}=D_{3q+2}\), and \(D_n\uparrow5/3\).

**Optimal-distance rigidity.** Rescale any optimal embedding into any real \(L_1\) space to be noncontracting. Its induced distances are then exactly \(2\) on all distinct same-part pairs and exactly \(D_n\) on all cross-part pairs. An explicit cut representation attaining this rigid distance profile is constructed below.

## Assumptions and scope

Distortion means the infimum, over injective maps \(f:X_n\to L_1\), of the ratio between the largest and smallest nonzero distance quotients \(\|f(x)-f(y)\|_1/d(x,y)\). As \(X_n\) is finite, all relevant \(L_1\) metrics have finite nonnegative cut representations. All edges have length one. The theorem is *not* a statement about worst distortion after changing edge weights, and no assertion is made for general \(K_{m,n}\) with \(m\ne3\).

For a subset \(S\subseteq X_n\), let \(\delta_S(x,y)=|\mathbf1_S(x)-\mathbf1_S(y)|\). For any symmetric function \(\rho\) vanishing on the diagonal, define \(U(\rho)\), \(V(\rho)\), and \(W(\rho)\) as its averages over unordered distinct pairs in \(A\), unordered distinct pairs in \(B\), and pairs in \(A\times B\), respectively.

## Proof

**1. A cut inequality.** If \(S\) contains \(a\in\{0,1,2,3\}\) vertices of \(A\) and \(b\in\{0,\dots,n\}\) of \(B\), count separated pairs to obtain

\[
U(\delta_S)=\frac{a(3-a)}3,\quad
V(\delta_S)=\frac{2b(n-b)}{n(n-1)},\quad
W(\delta_S)=\frac{a(n-b)+b(3-a)}{3n}.
\]

Define the rational function of an integer variable

\[
F_n(b)=\frac{n(n-1)-(2n+1)b+3b^2}{2n(n-1)}.
\]

Its real quadratic minimum is at \((2n+1)/6\). An integer minimizer on \(0\leq b\leq n\) is \(k=\lfloor(n+1)/3\rfloor\), with a tie between \(k\) and \(k+1\) exactly when \(n\equiv1\pmod3\). Write \(\alpha=F_n(k)\). For \(n\ge3\), \(\alpha>0\); for example, the numerator's unrestricted minimum is \((8n^2-16n-1)/12>0\).

For every cut, we claim

\[
\boxed{W(\delta_S)\ge\alpha U(\delta_S)+\tfrac12V(\delta_S).}
\]

For \(a=1\), subtract half the \(B\)-average from the cross-average and divide by the positive \(A\)-average \(2/3\). The resulting quotient equals \(F_n(b)\ge\alpha\). For \(a=2\), complementing the cut replaces \((a,b)\) with \((1,n-b)\), leaving all pair separations unchanged. For \(a=0\), the difference \(W-\tfrac12V\) is \(b(b-1)/(n(n-1))\ge0\); for \(a=3\), it is \((n-b)(n-1-b)/(n(n-1))\ge0\). This proves the inequality in all boundary cases, including empty or full cuts.

Every real \(L_1\) distance on a finite set is a nonnegative sum of cut semimetrics (decompose each real coordinate by threshold sets, then integrate). The inequality therefore holds for any induced \(L_1\) metric \(\rho\):

\[
W(\rho)\ge\alpha U(\rho)+\tfrac12V(\rho).
\]

After rescaling an embedding to be noncontracting and writing its distortion as \(D\), the graph distances give \(U(\rho)\ge2\), \(V(\rho)\ge2\), and \(W(\rho)\le D\). Hence

\[
D\ge2\alpha+1=2-\frac{k(2n+1-3k)}{n(n-1)}.
\]

**2. Exact matching cut embedding.** Let \(\Delta_{a,b}\) be the arithmetic average of \(\delta_S\) over all subsets \(S\) with \(|S\cap A|=a\) and \(|S\cap B|=b\). Set

\[
t=n-\frac{3k(n-k)}{n-1},\qquad
\rho_*=3\Delta_{1,k}+t\Delta_{0,1}.
\]

The coefficient \(t\) is nonnegative: for \(n\ge4\), use \(3k(n-k)\le3n^2/4\le n(n-1)\); for \(n=3\), \(k=1\) and \(t=0\). Thus \(\rho_*\) is a real \(\ell_1\) metric, explicitly represented in at most \(3\binom nk+n\) cut coordinates.

The first cut orbit contributes \(2/3\), \(2k(n-k)/(n(n-1))\), and \((n+k)/(3n)\) to the three averages, respectively; the second contributes \(0\), \(2/n\), and \(1/n\). Substitution gives

\[
U(\rho_*)=V(\rho_*)=2,\qquad
W(\rho_*)=2-\frac{k(2n+1-3k)}{n(n-1)}=2\alpha+1.
\]

The orbit averages have identical values on every pair of the same kind. Thus each same-part distance is exactly \(2\) and every cross-part distance is exactly \(D_n\). Since \(D_n>1\), this is a noncontracting embedding of distortion exactly \(D_n\), proving the reverse inequality.

**3. Rigidity and staircase.** Equality in the lower bound forces \(U(\rho)=V(\rho)=2\) because \(\alpha>0\), and forces \(W(\rho)=D_n\). Every same-part pair was individually bounded below by \(2\), while every cross-part pair was bounded above by \(D_n\); equality of their averages therefore implies the stated pointwise rigidity. Moreover, every nonnegative cut representation of an optimal metric can use only cuts at equality in the cut inequality (up to zero-weight cuts). The nontrivial equality profiles have either \((a,b)=(0,1)\), its complement, or \(a=1\) with \(b\) an integer minimizer of \(F_n\), or their complements.

Finally, substitute \(k=\lfloor(n+1)/3\rfloor\) separately for the three residue classes modulo three to obtain the displayed piecewise formula. It implies the exact two-step plateaus, strict increases between successive plateaus, and convergence to \(5/3\).

## Verification

The accompanying `verify_k3n.py` uses only Python's standard-library `fractions.Fraction`. It checks all cut inequality cases and the explicit optimal primal cut mixture for every integer \(3\le n\le300\), and independently constructs the cut ensemble by enumerating subsets for every \(3\le n\le9\). It reported `CHECK_OK 184728 exact rational assertions for n=3..300; direct cut enumeration n=3..9`. These are finite checks; the preceding case analysis and exact identities, not extrapolation, prove the theorem for all \(n\ge3\).

## Relationship to prior work

Abraham, Filtser, Gupta, and Neiman [1] motivate metric embeddings of graph shortest-path spaces and give general distortion estimates via shortest-path decompositions. Their investigated class and theorem are broader but quantitative bounds of a different kind; the inspected article does not supply the fixed unit-edge \(K_{3,n}\) formula, rigidity profile, or cut equality classification.

Mori [2] obtains the sharp worst-edge-weight \(\ell_1\) distortion of \(K_{2,n}\); the two-vertex-side family and the supremum over *all edge weights* are distinct from the three-vertex-side **fixed unit-weight** quantity computed here. Restriction to a two-vertex-side subgraph does not establish the sharp value for the full three-vertex-side graph. General flow-cut relations [3] and cut-metric geometry [4] provide context and tools but do not, by themselves, imply the all-parameter formula. Closely related published computational cut-cone examples concern other graph families. No historical priority or independence is claimed.

## Limitations

The classification applies only to the finite unit-edge \(K_{3,n}\) family with \(n\ge3\). It does not determine the worst distortion over arbitrary positive edge weights, the exact optimum for all \(K_{m,n}\), or a minimum-dimensional optimal embedding. Literature comparison was limited to accessible text and indexed findings; an equivalent result under alternative terminology may exist. No independent audit was performed.

## References

[1] I. Abraham, A. Filtser, A. Gupta, O. Neiman, *Metric Embedding via Shortest Path Decompositions*, arXiv:1708.04073v1 (first publicly posted 2017-08-14), https://arxiv.org/abs/1708.04073.

[2] H. Mori, *The exact value of \(c_1(K_{2,n})\)*, arXiv:2602.23745v1 (first publicly posted 2026-02-27), https://arxiv.org/html/2602.23745.

[3] A. Gupta, I. Newman, Y. Rabinovich, A. Sinclair, *Cuts, trees and \(\ell_1\)-embeddings of graphs*, Combinatorica 24 (2004), 233–269, DOI:10.1007/s00493-004-0015-x.

[4] M. Deza, M. Laurent, *Geometry of Cuts and Metrics*, Springer, 1997.
