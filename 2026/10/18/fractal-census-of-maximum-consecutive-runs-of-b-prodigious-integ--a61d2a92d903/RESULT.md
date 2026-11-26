# Shell census and Cantor law for longest runs of \(b\)-prodigious integers

## Finding

Fix a base \(b\ge3\). A positive integer \(n\) is \(b\)-prodigious if the product of its nonzero base-\(b\) digits divides \(n\). Let \(\ell_b=\min\{j\ge1:j\nmid b\}\). The known maximum run length is \(b+\ell_b\) [1]. An extremal start is the first integer of a run of that length. The contribution here is the quantitative census and distribution of those starts, using an elementary digit criterion derived from the known run classification.

Set
\[
 L_b=\operatorname{lcm}(1,\ldots,b-1),\qquad M_b=L_b/\gcd(L_b,b^2).
\]
Factor \(M_b=M_{0,b}M_{1,b}\), with all prime factors of \(M_{0,b}\) dividing \(b\) and \(\gcd(M_{1,b},b)=1\). Write \(r_b=\min\{r\ge0:M_{0,b}\mid b^r\}\). Let \(E_b(m)\) count extremal starts in \([b^{m+1},b^{m+2})\) for integers \(m\ge1\). If \(m\le r_b\), then \(E_b(m)=0\). Otherwise set \(h=m-r_b-1\). Then
\[
 E_b(m)=\#\left\{\varepsilon\in\{0,1\}^h:M_{1,b}\mid b^h+\sum_{j=0}^{h-1}\varepsilon_j b^j\right\}.
\]
For \(M=M_{1,b}>1\),
\[
 \left|E_b(m)-\frac{2^h}{M}\right|
 \le \frac{M-1}{M}\left(2\cos\frac{\pi}{M}\right)^h.
\]
The power at \(h=0\) is one by the empty-product convention; for \(M=1\), \(E_b(m)=2^h\) exactly.

Uniformly sampling an extremal start \(s\) in the \(m\)-th shell, the random variable \(s/b^{m+1}\) converges in distribution as \(m\to\infty\) to \(1+\sum_{j\ge1}\xi_j b^{-j}\), with independent fair bits \(\xi_j\). The limiting support has Hausdorff dimension \(\alpha_b=\log_b2\). If \(T_b(X)\) counts starts strictly below \(X\), then \(T_b(X)=\Theta_b(X^{\alpha_b})\), but
\[
 \lim_{m\to\infty}\frac{T_b(b^{m+2})}{(b^{m+2})^{\alpha_b}}=\frac{2^{-r_b-2}}{M_{1,b}},\qquad
 \lim_{m\to\infty}\frac{T_b(b^{m+2}/(b-1))}{(b^{m+2}/(b-1))^{\alpha_b}}=\frac{2^{-r_b-2}(b-1)^{\alpha_b}}{M_{1,b}}.
\]
The two constants are distinct for every \(b\ge3\).

## Proof

**Digit criterion (background reduction).** Gohn et al. [1, Corollary 4, Lemmas 7–8, Theorem 9] give the maximum length and a boundary classification from which a run of that length must start at \(s=b^2c\) with \(c>0\). For completeness, the boundary conclusion also follows directly. Write \(s=bk+r\), \(0\le r<b\). Two consecutive members of the same block \([bu,bu+b-1]\) force the digit product of the prefix \(u\) to be one (for \(u=0\) the prefix is empty), since it divides both members. Thus that prefix has only digits 0 and 1. Here \(2\le\ell_b\le b-1\), since \(b-1\nmid b\).

If \(r=b-1\), the run includes two numbers with final digit \(b-1\) separated by \(b\), which cannot both be divisible by \(b-1\). For \(0\le r\le b-2\) both of the first two blocks contain at least two terms, so \(k\) and \(k+1\) have digits in \(\{0,1\}\). Therefore the last digit of \(k\) is zero. If \(r>0\) and \(r+\ell_b\ge b+2\), a third block also contains at least two terms, contradicting the last digit 2 of \(k+2\). Otherwise, for \(r>0\) and \(r+\ell_b\le b+1\), the largest multiple \(j<b\) of \(\ell_b\) satisfies \(j\ge b-\ell_b+1\ge r\). The run contains \(bk+j\) and \(b(k+1)+\ell_b\); divisibility by their respective final digits forces \(\ell_b\) to divide both \(bk\) and \(b(k+1)\), impossible. Hence \(r=0\) and \(k=bc\) with \(c>0\).

The digit product of \(c\) divides both \(b^2c+1\) and \(b^2c+2\), so \(c\) has digits 0 and 1 only. Given those digits, membership of \(b^2c+j\) for \(1\le j<b\) is equivalent to \(j\mid b^2c\). The combined condition is \(L_b\mid b^2c\), exactly \(M_b\mid c\). Conversely, those conditions ensure membership of this first block (including \(b^2c\)). The product of the nonzero digits in \(b^2c+b+j\) is 1 if \(j=0\) and \(j\) for \(1\le j<\ell_b\); each such \(j\) divides both \(b\) and \(b^2c\). This proves the start criterion used in the census.

**Counting in a shell.** An \(m\)-digit binary-digit base-\(b\) integer \(c\) with exactly \(u\) trailing zero digits satisfies \(v_p(c)=u v_p(b)\) at every prime \(p\mid b\): the first nonzero digit after division by \(b^u\) is the units digit 1. Consequently \(M_{0,b}\mid c\) if and only if \(u\ge r_b\). Such \(c\) exist only if \(m>r_b\); write \(c=b^{r_b}d\), where \(d\) has leading digit 1 and \(h\) free binary digits. Since \(M_{1,b}\) is coprime to \(b\), its condition on \(c\) becomes \(M_{1,b}\mid d\). For \(M>1\), with \(\zeta=e^{2\pi i/M}\), the roots-of-unity filter gives
\[
 E_b(m)=\frac1M\sum_{t=0}^{M-1}\zeta^{t b^h}\prod_{j=0}^{h-1}(1+\zeta^{t b^j}).
\]
For \(t\ne0\) each factor has modulus at most \(2\cos(\pi/M)\), because no \(tb^j\) vanishes modulo \(M\). The \(t=0\) term gives the leading term, proving the error bound. When \(M=1\) every choice contributes.

**Distribution and global count.** The shell position is \(d/b^h\). Holding the first \(K\) bits after the leading digit fixed adds only a fixed residue offset; the filter on the other \(h-K\) bits gives \(2^{h-K}/M+o(2^h)\) completions, uniformly for fixed \(K\). Dividing by the shell asymptotic gives the fair Bernoulli probabilities on all fixed digit cylinders. These determine the weak limit because cylinder diameters tend to zero uniformly. The two similarity images of its support, of ratio \(1/b\), are separated, giving dimension \(\log_b2\).

Summing over the shells up to \(m\) gives \(T_b(b^{m+2})\sim 2^{m-r_b}/M\); the summed exponential errors are \(o(2^m)\). Each start in those shells is bounded above by \(b^2(b^m-1)/(b-1)<b^{m+2}/(b-1)\), while the next shell begins at \(b^{m+2}\). The two cutoffs therefore have the same count and give the two stated constants on division by their own powers. Monotone comparison between adjacent shell endpoints gives the stated two-sided power-law bounds.

## Scope and reproducibility

The result is for fixed integers \(b\ge3\), the nonzero-digit product, and maximal-length runs only. The effective Fourier bound need not be optimal. For example, in base 3 one has \(M=2,r_b=0\): for \(m\ge2\) exactly half the free-bit strings give even \(c\), so \(E_3(m)=2^{m-2}\); the first start is \(s=36\), with terms \(36,37,38,39,40\) having digit products \(1,1,2,1,1\). The existing optional `verify.py` in the supporting source gives finite integer illustrations; the formulas above require no numerical test.

## Relationship to prior work

The maximum run length and its boundary classification are [1]; the digit criterion is an elementary reformulation using that classification and is not a separate originality claim. Restricted-digit divisibility and residue-distribution methods are established, including [2]. The quantitative contribution is the base-dependent shell census for longest prodigious runs and its limiting positional and global counting consequences. [3] treats divisibility by the product of **all** digits, a different counting problem. [4] records decimal examples, including an extremal run of length 13, but not the general shell and distribution laws.

## References

1. M. Gohn, J. Harrington, S. Lebiere, H. Samamah, K. Shappell, T. W. H. Wong, *Arithmetic Progressions of b-Prodigious Numbers*, J. Integer Seq. 25 (2022), Article 22.8.7. https://cs.uwaterloo.ca/journals/JIS/VOL25/Wong/wong42.pdf
2. W. D. Banks, I. E. Shparlinski, *Arithmetic properties of numbers with restricted digits*, Acta Arith. 112 (2004), 313–332. DOI: 10.4064/aa112-4-1.
3. Q. He, C. Sanna, *Counting numbers that are divisible by the product of their digits*, arXiv:2403.14812v1.
4. OEIS A055471, numbers divisible by the product of their nonzero decimal digits. https://oeis.org/A055471
