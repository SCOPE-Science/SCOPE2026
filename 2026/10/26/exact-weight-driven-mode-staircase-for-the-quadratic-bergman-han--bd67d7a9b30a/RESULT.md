# Exact weight-driven mode staircase for the quadratic Bergman Hankel operator

## Finding

For every \(\alpha>-1\), put \(\beta=\alpha+2>1\). On the standard weighted analytic Bergman space \(A^2_\alpha(\mathbb D)\), let \(H_\alpha f=(I-P_\alpha)(\overline z^{\,2}f)\), where \(P_\alpha\) is the orthogonal projection from weighted \(L^2\) onto \(A^2_\alpha\). For each integer \(k\ge1\), define
\[
 B_k=\frac{k+3+\sqrt{9k^2+18k+1}}{2},\qquad B_0=1.
\]
These thresholds are strictly increasing to infinity. For \(B_{k-1}<\beta<B_k\), the unique norming input ray for \(H_\alpha\) is the normalized monomial \(z^k\); at \(\beta=B_k\), the complete norming input subspace is \(\operatorname{span}\{z^k,z^{k+1}\}\). Thus the maximizer makes one-step jumps at every \(B_k\), with no other degeneracies. For \(\beta\) in an open staircase interval, the squared sharp operator norm is
\[
 \|H_\alpha\|^2=\frac{2(\beta-1)(2\beta k+\beta+2k^2-2)}{(\beta+k-2)(\beta+k-1)(\beta+k)(\beta+k+1)}.
\]
At a threshold either of the two adjacent indices gives the same value. Every norm-attaining nonzero input is exactly a nonzero member of the indicated subspace. As \(\beta\to\infty\), any maximizing degree is \(\beta/2+O(1)\), and
\[
 \|H_\alpha\|^2=\frac{16}{27\beta}+O(\beta^{-2}).
\]
Moreover, the degree-one symbol has \(\|H_{\overline z}\|^2=1/\beta\), and the quadratic-symbol norm is strictly larger, equal, or strictly smaller according as \(1<\beta<2\), \(\beta=2\), or \(\beta>2\). Here \(H_{\overline z}f=(I-P_\alpha)(\overline z f)\) on the same domain.

## Assumptions and scope

The disk \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) carries the probability measure
\[
 d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dA(z),\quad \alpha>-1.
\]
The operator is the **big** anti-analytic-symbol Hankel operator from analytic \(A^2_\alpha\) to \(L^2(\mu_\alpha)\ominus A^2_\alpha\), not a little Hankel operator or a Hardy-space Hankel matrix. Norming subspaces are complex linear; a norming vector may be any nonzero complex combination of the listed monomials at a double crossing. The exponent \(\alpha\) is real, not restricted to integers. All statements concern the full infinite-dimensional operator.

## Proof

**Orthogonal singular channels.** For each integer \(n\ge0\), define
\[
 m_n=\int_{\mathbb D}|z|^{2n}\,d\mu_\alpha(z)=\frac{n!\,\Gamma(\beta)}{\Gamma(n+\beta)},\qquad e_n(z)=z^n/\sqrt{m_n}.
\]
The monomials \(e_n\) form an orthonormal basis. Since \(\overline z^{\,2}z^n\) has angular frequency \(n-2\), the outputs \(H_\alpha e_n\) are mutually orthogonal as \(n\) varies. Direct projection and Pythagoras therefore give \(H_\alpha^*H_\alpha e_n=s_n^2 e_n\), where
\[
 s_n^2=\frac{m_{n+2}}{m_n}-\mathbf1_{\{n\ge2\}}\frac{m_n}{m_{n-2}}.
\]
In particular \(s_0^2=2/[\beta(\beta+1)]\), and simplifying the moment ratios gives, for every integer \(n\ge1\),
\[
 s_n^2=\frac{2(\beta-1)(2\beta n+\beta+2n^2-2)}{(\beta+n-2)(\beta+n-1)(\beta+n)(\beta+n+1)}.
\]
This formula also holds for \(n=1\): the potentially exceptional projection term is zero and no denominator vanishes for \(\beta>1\). In particular \(s_1^2=6/[(\beta+1)(\beta+2)]\), and \(s_1^2/s_0^2=3\beta/(\beta+2)>1\). The explicit rational formula yields \(s_n^2=4(\beta-1)n^{-2}+O_\beta(n^{-3})\) as \(n\to\infty\); hence \(H_\alpha\) is compact, and its norm is the largest \(s_n\).

**Exactly one peak and all crossing weights.** For every integer \(n\ge1\), subtraction and factorization give
\[
 s_{n+1}^2-s_n^2=\frac{4(\beta-1)Q_n(\beta)}{(\beta+n-2)(\beta+n-1)(\beta+n)(\beta+n+1)(\beta+n+2)},
\]
where \(Q_n(\beta)=\beta^2-(n+3)\beta-2n^2-3n+2\). The denominator is strictly positive. For fixed \(n\ge1\), \(Q_n\) has exactly one positive zero \(B_n\), since its constant term is negative; solving the quadratic gives the stated expression. The thresholds strictly increase: both \(k+3\) and \(9k^2+18k+1\) do. For each fixed \(\beta>1\), \(Q_n(\beta)\) decreases strictly in integer \(n\ge1\), since \(Q_{n+1}-Q_n=-\beta-4n-5<0\). Thus \(s_n^2\) strictly rises, possibly has one adjacent tie, and then strictly falls. Together with \(s_1^2>s_0^2\), this proves the sharp norm, the exact staircase intervals and the entire norming eigenspaces, with no undiscovered high-degree competitor.

**Asymptotic winning mode.** The real zero of \(Q_n(\beta)\), viewed as a quadratic in \(n\), is
\[
 n_*(\beta)=\frac{-(\beta+3)+\sqrt{9\beta^2-18\beta+25}}4=\frac\beta2-\frac32+O(\beta^{-1}).
\]
The maximizing integer differs from \(n_*\) by at most one, so is \(\beta/2+O(1)\). Substituting this scale into the exact rational channel eigenvalue gives \(s_n^2=16/(27\beta)+O(\beta^{-2})\), uniformly for bounded differences between \(n\) and \(\beta/2\).

**Comparison with the linear symbol.** For \(\overline z\), the channel squares are \((\beta-1)/[(n+\beta)(n+\beta-1)]\) for every \(n\ge0\) (including \(n=0\)); the largest is \(1/\beta\), at \(n=0\). For \(1<\beta<2\), the quadratic peak is at \(n=1\), and \(s_1^2-1/\beta=-(\beta-1)(\beta-2)/[\beta(\beta+1)(\beta+2)]>0\). For \(\beta\ge2\), \(s_0^2<1/\beta\). For \(n\ge1\), write \(u=\beta-2\ge0\) and \(x=n-1\ge0\). After multiplication by the positive denominator \(\beta(\beta+n-2)(\beta+n-1)(\beta+n)(\beta+n+1)\), the quantity \(1/\beta-s_n^2\) is exactly
\[
 u^4+4u^3+5u^2+2u+2u^2x^2+2u^2x+4ux^3+18ux^2+14ux+x^4+10x^3+27x^2+18x.
\]
All terms are nonnegative, with equality exactly at \(u=x=0\), i.e. \(\beta=2,n=1\). This proves the strict reversal and its unique equality parameter.

## Verification

The included standalone `checker.py` uses exact rational arithmetic to compare moment-ratio channel norms with the rational closed formula, verifies adjacent-difference identities, and compares the predicted peak against exhaustive finite lists for rational test weights whose predicted peak lies in the list. It also tests the strict degree-one-versus-degree-two norm reversal. The script is supplementary to the infinite-dimensional proof; no finite sample can prove a universal spectral statement. Reproduce with `python3 checker.py` using the standard library.

## Relationship to prior work

Keshavarzi and Wu, arXiv:2210.06896 (public since 2022-10-13), characterize Schatten membership of Hankel operators on regular weighted Bergman spaces through mean oscillation. Bourass, El-Fallah, Marrhich and Naqos, arXiv:2102.01743 (2021-02-02), study singular-value decay, including the linear-symbol case; their asymptotic claims do not yield the largest singular value and its maximizing degree for the quadratic symbol at every weight. Janson's *Hankel operators between weighted Bergman spaces* develops boundedness/compactness/Schatten membership in a wider two-weight setting; the inspected statements do not give these sharp weight thresholds. Existing mathematical-result indexing includes weighted **harmonic** Bergman circle-trace frequency staircases, but those are different operators and parameters. These are statement-and-implication distinctions, not a claim that keyword search proves global novelty.

## Limitations

The formula classifies the quadratic anti-analytic monomial symbol only; it does not classify arbitrary analytic symbols or all monomial degrees. The proof is self-contained, but a complete historical priority determination against all early operator-norm literature has not been established. The referenced general theory may provide unexploited alternative derivations; the exact staircase is not claimed to require a new general-purpose method.

## References

1. H. Keshavarzi and F. Wu, *Schatten Class Hankel Operators on Weighted Bergman Spaces induced by regular weights*, arXiv:2210.06896, first public 2022-10-13, https://arxiv.org/abs/2210.06896.
2. M. Bourass, O. El-Fallah, I. Marrhich and H. Naqos, *On singular values of Hankel operators on Bergman spaces*, arXiv:2102.01743, first public 2021-02-02, https://arxiv.org/abs/2102.01743.
3. S. Janson, *Hankel operators between weighted Bergman spaces*, Arkiv för Matematik 26 (1988), https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/7489-11512_2006_Article_BF02386120.pdf.
4. J. Arazy, S. D. Fisher and J. Peetre, *Hankel operators on weighted Bergman spaces*, American Journal of Mathematics 110 (1988), 989–1053, doi:10.2307/2374685 (priority comparison limited by full-text access).
