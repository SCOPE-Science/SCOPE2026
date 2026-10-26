# Exact two-sided fourth moments and ternary phase resonance for paired symmetric-power characters of \(SU(3)\)

## Finding

Let \(G=SU(3)\) carry probability Haar measure. For each integer \(n\ge2\), let \(\chi_n(g)=\operatorname{tr}(\operatorname{Sym}^n g)\) be the ordinary (unnormalized) irreducible trace character of highest weight \((n,0)\). Put
\[
F_{a,b}(g)=a\chi_n(g)+b\overline{\chi_n(g)},\qquad S=|a|^2+|b|^2>0.
\]
Define the fourth-power ratio \(Q_n(a,b)=S^{-2}\int_G|F_{a,b}|^4\,dg\). Its **exact sharp two-sided bounds** are as follows:
\[
\boxed{\begin{array}{ll}
 n\not\equiv0\pmod3:& n+1\le Q_n(a,b)\le \frac32(n+1),\\[2mm]
 n\equiv0\pmod3:& n+1-\frac{2}{n+2}\le Q_n(a,b)\le \frac32n+4.
\end{array}}
\]
All four endpoints are attained, and all equality cases are:

- If \(3\nmid n\), the minimum requires \(ab=0\). The maximum requires \(|a|=|b|>0\), with arbitrary relative phase.
- If \(3\mid n\), the maximum requires \(a=b\ne0\). The minimum requires \(a\overline b\) to be negative real and \(|ab|/S=1/(n+2)\). Equivalently, \(a/b\) is one of the two negative real roots of \(r^2+(n+2)r+1=0\).

The full phase-sensitive fourth-moment identity is, with \(\delta_n=1\) if \(3\mid n\) and \(\delta_n=0\) otherwise,
\[
\boxed{\int_G|F_{a,b}|^4\,dg
=(n+1)(S^2+2|ab|^2)
+\delta_n\left[4S\operatorname{Re}(a\overline b)+2\operatorname{Re}(a^2\overline b^{\,2})\right].}
\]
Thus divisibility by three activates phase interference: only in that case can mixing conjugate characters improve on the pure-character minimum. These statements apply to the entire canonical two-dimensional span, with no real-coefficient restriction.

## Assumptions and scope

The group is the compact matrix group \(SU(3)\) with normalized Haar measure. The representation \(\operatorname{Sym}^n\mathbb C^3\) is irreducible with highest weight \((n,0)\); its dual has highest weight \((0,n)\) and is inequivalent for \(n\ge1\). Hence the two characters are orthonormal in Haar \(L^2(G)\) and \(\|F_{a,b}\|_2^2=S\). All coefficients are arbitrary complex numbers, not simultaneously zero. The claim covers all integers \(n\ge2\), with no limiting regime.

## Proof

**1. Four exact character moments.** For \(n\ge1\), write \(V_n=\operatorname{Sym}^n\mathbb C^3\) and \(\chi=\chi_n\). Character orthogonality gives \(\int_G|\chi|^2\,dg=1\). The Pieri decomposition
\[
V_n\otimes V_n\cong\bigoplus_{j=0}^{n}V_{(2n-2j,j)}
\]
contains \(n+1\) pairwise inequivalent irreducible representations, each with multiplicity one. (The displayed weights are Dynkin coordinates, corresponding to three-row partitions \((2n-j,j,0)\).) Thus
\[
\int_G|\chi|^4\,dg=n+1.
\]
The center of \(SU(3)\) acts on \(V_n\) through the character \(\omega\mapsto\omega^n\). Consequently the two moments \(\int_G\chi^3\overline\chi\,dg\) and \(\int_G\chi^4\,dg\) vanish unless \(3\mid n\).

For \(n=3q\), the first of those moments is the multiplicity of \(V_n\) in \(V_n^{\otimes3}\). In the corresponding \(GL_3\) tensor product of degree \(3n\), the only partition restricting to highest weight \((n,0)\) is \((5q,2q,2q)\). After the first two Pieri factors, an intermediate partition is \((6q-j,j,0)\), \(0\le j\le3q\). The last horizontal strip must interlace \((5q,2q,2q)\), forcing \(j=2q\), and that choice is admissible. This multiplicity equals one.

The second moment counts the trivial representations in \(V_n^{\otimes4}\). Its required \(GL_3\) partition is uniquely \((4q,4q,4q)\). The preceding three-factor partition must be \((4q,4q,q)\) by horizontal-strip interlacing and total degree \(9q\); at the preceding step the only admissible partition is \((4q,2q,0)\). Thus this multiplicity is also exactly one. In summary,
\[
\int_G\chi^3\overline\chi\,dg
=\int_G\chi^4\,dg=\delta_n.
\]
These are exact representation-multiplicity identities, not asymptotics.

**2. Exact quartic form.** Expanding \(F_{a,b}^2\overline{F_{a,b}}^{\,2}\), the only nonzero character integrals are the four just computed and their conjugates. This gives the boxed fourth-moment identity in the Finding section without discarding any cross term.

**3. Optimization and complete equality.** Divide by \(S\) and put \(r=|ab|/S\in[0,1/2]\). When \(r>0\), write \(a\overline b/S=r e^{i\theta}\). If \(3\nmid n\), the quotient is \((n+1)(1+2r^2)\), strictly increasing in \(r\), so both bounds and equality cases follow.

If \(3\mid n\), the quotient is
\[
Q_n=(n+1)+2nr^2+4r^2\cos^2\theta+4r\cos\theta.
\]
At each fixed \(r\le1/2\), the convex quadratic in \(x=\cos\theta\in[-1,1]\) is maximized at \(x=1\) and minimized at \(x=-1\); indeed its stationary point is \(x=-1/(2r)\le-1\). Therefore
\[
(n+1)+2(n+2)r^2-4r\ \le Q_n\le\ (n+1)+2(n+2)r^2+4r.
\]
The upper expression increases to \(\frac32n+4\) at \(r=1/2\). The lower quadratic is uniquely minimized at \(r=1/(n+2)\), with value \(n+1-2/(n+2)\). The relative phase and product-to-sum ratios force precisely the equality cases listed above. Continuity includes \(r=0\), and no other boundary cases produce equality.

## Verification

An independent Laurent-polynomial implementation of the Weyl integration formula calculates all four source moments with **exact integer arithmetic** for every \(1\le n\le10\). It reproduces \((1,n+1,\delta_n,\delta_n)\). The standalone `CHECKER.py` uses only the Python standard library and runs as `python CHECKER.py`. The mathematical proof is the Pieri argument above; finite checking is corroboration, not an exhaustive substitute for it.

## Relationship to prior work

Schur orthogonality, Pieri multiplication and the Weyl integration formula are classical. Issa, Abbas and Mourad give integral formulas for traces of symmetric tensor powers of matrices; these are not the same as two-sided Haar fourth-moment optimization for conjugate \(SU(3)\) character pairs. Lee and Oh evaluate characteristic-polynomial correlations over certain proper subgroups of \(U(3)\), while Agarwal and Nahmgoong count invariant tensors built from adjoint representations; neither result states the two-sided all-\(n\) inequality here. An earlier finite-dimensional sharp calculation for the fundamental, antifundamental and adjoint \(SU(3)\) characters addresses fixed lowest weights, not the higher symmetric-power family or the divisibility-by-three transition. The present statement claims the complete higher-weight sharp bounds and equality cases, not the underlying representation-theoretic tools.

## Limitations

The result is specific to the canonical pair \(\chi_n,\overline\chi_n\) in \(SU(3)\), and to the fourth moment; it does not classify larger character packets, higher moments, or other compact groups. The computed moment formulas use classical representation theory and may be obtainable as unstated corollaries of broader invariant-theory literature. A focused literature comparison did not establish full historical priority. The equality statements are exact mathematical claims and do not imply independent external verification.

## References

1. H. Issa, H. Abbas and B. Mourad, *On an integral representation of the normalized trace of the k-th symmetric tensor power of matrices and some applications*, arXiv:2106.01486v1 (first posted 2021-06-02), https://arxiv.org/abs/2106.01486.
2. K.-H. Lee and S. Oh, *Auto-correlation functions for unitary groups*, arXiv:2110.00505v1 (first posted 2021-10-01), https://arxiv.org/abs/2110.00505.
3. P. Agarwal and J. Nahmgoong, *Singlets in the tensor product of an arbitrary number of Adjoint representations of SU(3)*, arXiv:2001.10826v1 (first posted 2020-01-23), https://arxiv.org/abs/2001.10826.
4. I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, second edition, Oxford University Press, 1995 (Pieri multiplication rule).
