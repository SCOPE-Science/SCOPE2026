# Sharp oscillatory \(c\)-marker correlations in a one-sided-balanced coded shift
## Finding
Let \(X\subset\{a,b,c\}^{\mathbb Z}\) be the shift-space closure of bi-infinite concatenations of words in
\[
\mathcal C=\{a^j b^j:j\ge1\}\cup\{a^\ell b^m c:\ell>m\ge1\}\cup\{c\}.
\]
For the shift \(\sigma\), there is exactly one measure of maximal entropy \(\mu\), and it is fully supported. Set \(A=\{x:x_0=c\}\) and \(C_n=\mu(A\cap\sigma^{-n}A)-\mu(A)^2\) for \(n\ge0\). Then \(\mu(A)=2/7\) and, as a convergent power series near zero,
\[
\boxed{\sum_{n\ge0}C_nz^n=-\frac{8(3z^2-3z-10)}{49(z^3-2z^2+8)}.}
\]
Let \(r\in(-1.51,-1.50)\) be the unique real root of \(Q(z)=z^3-2z^2+8\). Put \(\gamma=1/r\) and \(\eta=\sqrt{|r|/8}\). Then
\[
\boxed{C_n=\kappa\gamma^n+O(\eta^n),\qquad
\kappa=\frac{8(3r^2-3r-10)}{49r(3r^2-4r)}\ne0.}
\]
Numerically \(\gamma\approx-0.662358978622373\), \(\eta\approx0.434418480916355\), and \(\kappa\approx-0.011482822103502\). Thus correlations of the canonical synchronizing marker are eventually alternating and have the sharp exponential rate \(\lim_{n\to\infty}|C_n|^{1/n}=|\gamma|\).

## Assumptions and scope
The alphabet consists of three distinct letters, and all exponents in the generating code are positive integers subject to the displayed inequalities. The shift is two-sided. The measure is shift-invariant, Borel, and probability-valued. The correlation concerns exactly the cylinder \(x_0=c\), not arbitrary test functions. Neither a general mixing rate nor a new entropy formula is claimed.

## Proof
**1. Unique first returns to the marker.** Every finite return block from one occurrence of \(c\) to the next consists of zero or more balanced code words \(a^jb^j\), followed by exactly one terminal word \(c\) or \(a^\ell b^mc\) with \(\ell>m\). Each boundary between balanced words is read from \(ba\), and the final \(c\) identifies the terminal block. Thus this parsing is unique. The balanced and terminal generating series, counted by word length, are
\[
B(t)=\sum_{j\ge1}t^{2j}=\frac{t^2}{1-t^2},\qquad
E(t)=t+\sum_{\ell>m\ge1}t^{\ell+m+1}
=t+\frac{t^4}{(1-t)(1-t^2)}.
\]
The generating series for first-return blocks (including their terminal \(c\)) is
\[
R(t)=\frac{E(t)}{1-B(t)}
=\frac{t(2t^3-t^2-t+1)}{(t-1)(2t^2-1)}.
\]
In particular, \(B(1/2)=1/3\), \(E(1/2)=2/3\), \(R(1/2)=1\), and \((tR'(t))|_{t=1/2}=7/2\). Assign each return block \(w\) probability \(q(w)=2^{-|w|}\). This is a probability distribution of finite mean length \(7/2\). The stationary version of the i.i.d. concatenation of these return blocks defines an invariant measure \(\mu\); because every admissible finite block occurs in a concatenation containing \(c\), every nonempty cylinder has positive measure. The marked renewal density is \(\mu(A)=1/(7/2)=2/7\).

**2. Entropy maximality and uniqueness.** A length-\(n\) word in \(X\) is a concatenation of at most two partial code words around zero or more complete code words. The number of distinct partial-code fragments of each length grows polynomially: each fragment has at most one internal \(a\)-to-\(b\) transition, or is a segment of a balanced word. The number \(f_k\) of concatenations of complete code words of length \(k\) satisfies \(f_k2^{-k}\le1\), because the code probabilities \(2^{-|w|}\) sum to \(B(1/2)+E(1/2)=1\). Therefore the language size is at most a polynomial in \(n\) times \(2^n\), and \(h_{\rm top}(X)\le\log2\).

Any ergodic invariant probability \(\nu\) with \(\nu(A)>0\) induces, by return to \(A\), a stationary process on first-return blocks. Its mean return length is \(1/\nu(A)\) by Kac's formula; the inducing entropy identity (Abramov's formula) gives \(h_\nu(\sigma)=h_{\mathrm{ind}}/\mathbb E_\nu L\). Denote the return-block marginal by \(p_w\). Entropy rate is bounded by one-block Shannon entropy, and nonnegativity of relative entropy with respect to \(q_w=2^{-|w|}\) implies
\[
h_{\mathrm{ind}}\le H(p)\le(\log2)\sum_wp_w|w|.
\]
Both inequalities are equalities exactly when the return-block process is i.i.d. with marginal \(q\). For this process, induced entropy is \(\frac72\log2\); hence \(h_\mu(\sigma)=\log2\), proving maximality and the exact topological entropy.

If \(\nu(A)=0\), its support lies in the subshift forbidding \(c\). A word in that subshift consists of at most two partial \(a\)/\(b\) blocks separated by concatenated balanced words, whose length-generating series is \(B(t)\) and whose growth exponent is \(\frac12\log2\). Boundary fragments contribute only a polynomial factor. Thus \(h_\nu\le\frac12\log2<\log2\). Every ergodic maximal measure therefore has \(\nu(A)>0\), and equality above forces precisely the stationary i.i.d. \(q\) renewal law, namely \(\mu\). Ergodic decomposition extends uniqueness to all invariant measures.

**3. Exact covariance series.** Conditioned on observing \(c\) at the origin under \(\mu\), subsequent markers are renewals with independent increments of generating function \(R(z/2)\). Let \(u_n=\mu(x_n=c\mid x_0=c)\), with \(u_0=1\). Its generating series is
\[
U(z)=\sum_{n\ge0}u_nz^n=\frac1{1-R(z/2)}
=-\frac{2(z-2)(z^2-2)}{(z-1)(z^3-2z^2+8)}.
\]
Because \(C_n=(2/7)(u_n-2/7)\), subtracting the stationary pole at \(z=1\) gives
\[
\sum_{n\ge0}C_nz^n
=\frac27\left(U(z)-\frac{2}{7(1-z)}\right)
=-\frac{8(3z^2-3z-10)}{49Q(z)}.
\]
The first three coefficients are \(C_0=10/49\), \(C_1=3/49\), and \(C_2=-1/98\).

**4. Sharp pole asymptotic.** Since \(Q'(z)=z(3z-4)\), the cubic is strictly increasing on the negative real half-line, and it has one negative root \(r\in(-1.51,-1.50)\). Its positive local minimum \(Q(4/3)=184/27>0\) shows that its remaining roots are a conjugate pair of modulus \(\sqrt{8/|r|}>|r|\). All poles are simple. The numerator is nonzero at \(r\) because \(3r^2-3r-10>0\) throughout this interval. Extracting the coefficient from the simple pole gives \(\kappa=-N(r)/(rQ'(r))\), where \(N(z)=-8(3z^2-3z-10)/49\). The other two poles yield an exponentially smaller \(O((\sqrt{|r|/8})^n)\) contribution. This proves the claimed asymptotic, its nonzero leading coefficient, eventual alternating signs, and sharp rate.

## Verification
Run `python checker.py` with Python's standard library. It compares independently enumerated first-return words with the renewal recursion through length \(90\), verifies the first \(91\) covariance coefficients exactly as fractions against the rational generating series, and checks the probability normalization \(R(1/2)=1\). The infinite classification, entropy uniqueness and pole estimate are established by the proof, not by these finite tests.

## Relationship to prior work
Hong and Kim introduce precisely this one-sided-balanced, not left-balanced, coded shift as their Example 3.5 and analyze balance and word growth. The entropy bound and return-word formalism here are used as inputs, not represented as new general theories. Countable-state thermodynamic formalism and renewal theory provide standard tools. The object-specific rational covariance, nonzero oscillatory leading term, and sharp marker-correlation rate are the proposed new quantitative result. Earlier work on avoidance exponents in bi-balanced shifts assumes a property this system explicitly lacks, so that theorem does not imply the present return-correlation calculation.

## Limitations
The autocovariance concerns a single canonical marker and one maximal-entropy measure. It does not assert the same asymptotic for every cylinder or global correlation decay for all observables. The published source's Example 3.5 and surrounding material were examined in available indexed text, but equivalence to an older unindexed calculation is a residual priority risk. Independent mathematical validation has not been performed.

## References
1. S. Hong and M. Kim, *Bi-balanced shifts and variable specification*, arXiv:2609.33476v1 (first posted 2026-09-27), Example 3.5.
2. O. Sarig, *Thermodynamic formalism for countable Markov shifts*, Ergodic Theory Dynam. Systems 19 (1999), 1565–1593, doi:10.1017/S0143385799146820 (general context).
3. Standard Kac return-time and Abramov entropy formulas; used only in their stated measure-preserving inducing forms.
