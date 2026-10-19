# Exact ordinary and logarithmic density laws for exceptional Fibonacci block-entropy lengths

## Finding
Let \(\varphi=(1+\sqrt5)/2\), \(\alpha=\varphi^{-1}\), and let \(\mu\) be the unique invariant probability on the two-sided Fibonacci Sturmian shift, equivalently the binary coding of irrational rotation by \(\alpha\) with its natural two-interval partition. For each integer \(n\ge1\), the \(n+1\) nonzero length-\(n\) cylinder probabilities are denoted \(\mu[w]\). For every real Rényi order \(q>0\), define
\[
H_q(n)=\begin{cases}
\displaystyle\frac{\log\sum_{|w|=n}\mu[w]^q}{1-q},&q\ne1,\\[3pt]
\displaystyle-\sum_{|w|=n}\mu[w]\log\mu[w],&q=1,
\end{cases}
\qquad D_q(n)=\log(n+1)-H_q(n).
\]
All logarithms are natural. The deficit \(D_q(n)\) measures how far the true word-frequency distribution lies below the uniform distribution on its \(n+1\) allowed words. Put
\[
u=\varphi^{-1},\quad v=\varphi^{-2},\quad
a=\frac{\varphi^2}{\sqrt5},\quad b=\frac{\varphi}{\sqrt5},\quad c=\frac1{\sqrt5},\quad 0\le t\le u.
\]
Define a continuous profile
\[
d_q(t)=\begin{cases}
\displaystyle\log(1+t)-\frac{\log\big((u-t)a^q+(v+t)b^q+t c^q\big)}{1-q},&q\ne1,\\[4pt]
\displaystyle\log(1+t)+(u-t)a\log a+(v+t)b\log b+t c\log c,&q=1.
\end{cases}
\]
For every fixed \(q>0\), the endpoints agree, \(d_q(0)=d_q(u)=:\delta_q\); the profile has exactly one interior maximizer \(t_q\in(0,u)\), with \(M_q=d_q(t_q)>\delta_q\). Explicitly,
\[
t_q=\frac{(1-q)(u a^q+v b^q)-(-a^q+b^q+c^q)}{q(-a^q+b^q+c^q)}\quad(q\ne1),
\qquad t_1=-1-\frac1{-a\log a+b\log b+c\log c}.
\]
Fix **any** \(q>0\) and **any** \(\theta\) satisfying \(\delta_q<\theta<M_q\). There are unique \(0<t_-<t_q<t_+<u\) such that \(d_q(t_-)=d_q(t_+)=\theta\). Define the set of exceptional observation lengths
\[
E_{q,\theta}=\{n\ge1:D_q(n)>\theta\},\qquad L=t_+-t_-.
\]
**The complete counting-density result is**
\[
\boxed{\liminf_{N\to\infty}\frac{|E_{q,\theta}\cap[1,N]|}{N}
=\frac{\varphi L}{1+t_-},\qquad
\limsup_{N\to\infty}\frac{|E_{q,\theta}\cap[1,N]|}{N}
=\frac{\varphi^2 L}{1+t_+}.}
\]
The two limits are strictly different, so no ordinary natural density exists, and every intermediate value is an accumulation point of the empirical densities. In contrast, the **logarithmic density exists**, with the exact value
\[
\boxed{\lim_{N\to\infty}\frac1{\log N}
\sum_{\substack{n\le N\\ n\in E_{q,\theta}}}\frac1n
=\frac{\log\big((1+t_+)/(1+t_-)\big)}{\log\varphi}.}
\]
In particular, the existence of the logarithmic density does not imply the existence of the natural density, even for these canonical stationary word-frequency statistics. The result holds simultaneously as a theorem for every fixed positive order and every nontrivial threshold; no numerical cutoff is part of the statement.

## Assumptions and scope
The subshift is the two-sided orbit closure of the fixed point of \(0\mapsto01\), \(1\mapsto0\), with unique invariant measure given by the golden irrational rotation. Cylinder lengths are integer \(n\ge1\), and counts in \([1,N]\) refer to **word lengths**, not locations inside a word or points of a dynamical orbit. We use \(F_0=0\), \(F_1=1\), \(F_{j+1}=F_j+F_{j-1}\). Asymptotics let \(N\) tend to infinity through all positive integers. The threshold must lie strictly between the common endpoint deficit and the unique profile maximum. No claim is made at threshold equality or for \(q\le0\).

## Proof
**1. Exact finite-block input.** A length-\(n\) binary rotation cylinder is an arc between successive points of \(\{0,\alpha,\ldots,n\alpha\}\) modulo one. This classical coding fact and the complete three-distance frequency theorem are prior mathematics [2,3]. Set \(B=n+1\). For the unique \(j\ge3\) and \(0\le k<F_{j-1}\) such that \(B=F_j+k\), their golden-ratio specialization states that the circle partition has exactly
\[
\begin{array}{c|c}
\text{arc length (cylinder probability)}&\text{multiplicity}\\ \hline
\alpha^{j-2}&F_{j-1}-k\\
\alpha^{j-1}&F_{j-2}+k\\
\alpha^j&k.
\end{array}
\tag{1}
\]
For completeness, an elementary inductive route to (1) uses the identity \(\{F_j\alpha\}=\alpha^j\) for odd \(j\) and \(\{F_j\alpha\}=1-\alpha^j\) for even \(j\). At \(B=F_j\), the long arcs have length \(\alpha^{j-2}=\alpha^{j-1}+\alpha^j\) and their relevant forward endpoints (odd \(j\)) or backward endpoints (even \(j\)) are indexed by \(0,\ldots,F_{j-1}-1\). Inserting the next \(k\) orbit points splits \(k\) distinct long arcs into the two shorter types; the same endpoint property changes orientation at \(B=F_{j+1}\). The base \(B=F_3=2\) is immediate. This is an exact explanation of the already-known three-distance specialization, not a novelty claim. Therefore, for all finite \(n\), every Rényi entropy is obtained by substituting (1), with the Shannon case read as its \(q=1\) limit.

**2. Uniform Fibonacci-scale entropy profile.** Let \(j\to\infty\), \(0\le k<F_{j-1}\), and write \(t=k/F_j\). Binet's formula gives, uniformly across these \(k\),
\[
\frac{F_{j-1}}{F_j}=u+O(\varphi^{-2j}),\quad
\frac{F_{j-2}}{F_j}=v+O(\varphi^{-2j}),\quad
F_j\alpha^{j-2}=a+O(\varphi^{-2j}),
\]
with analogous formulas for \(b,c\). Using \(B=F_j(1+t)\) and normalization of the cylinder lengths, substitution in the Rényi formulas establishes
\[
\sup_{0\le k<F_{j-1}}\big|D_q(F_j+k-1)-d_q(k/F_j)\big|\longrightarrow0.
\tag{2}
\]
This is valid for each fixed \(q>0\), including \(q=1\). It is uniform over the entire Fibonacci block, not merely along selected subsequences.

**3. Shape and threshold crossing.** Write \(s_0=u a^q+v b^q\) and \(s_1=-a^q+b^q+c^q\). For \(q\ne1\), \(d_q(t)=\log(1+t)-\log(s_0+s_1t)/(1-q)\). The identities \(a=b+c\) and \(1+u=\varphi\), together with \(a/\varphi=b\) and \(b/\varphi=c\), give \(d_q(0)=d_q(u)\). For \(q>1\), \(s_1<0\); for \(0<q<1\), \(s_1>0\), by strict convexity or concavity of positive powers. In both cases the numerator of \(d_q'\) is a strictly decreasing affine function of \(t\): its slope is \(-q s_1/(1-q)<0\). Since the endpoint values agree and the derivative is not identically zero, it has one zero in \((0,u)\), and the profile rises strictly then falls strictly. Solving \(d_q'(t)=0\) gives the displayed \(t_q\). At \(q=1\), \(d_1''(t)=-(1+t)^{-2}<0\), and endpoint equality again gives a unique interior maximum. Thus every permitted threshold has exactly two transverse crossings.

**4. Counts inside and between Fibonacci blocks.** By (2), continuity, and the transverse crossings, the selected lengths \(n=F_j+k-1\), \(0\le k<F_{j-1}\), occupy the interval \(t_-<k/F_j<t_+\) up to \(o(F_j)\) exceptions in each block. In particular,
\[
\#\big(E_{q,\theta}\cap[F_j-1,F_{j+1}-2]\big)
=L F_j+o(F_j).
\tag{3}
\]
Fix \(s\in[1,\varphi]\), choose any cutoff \(N_j\) with \(N_j/F_j\to s\), and let \(\operatorname{clip}(x;0,L)=\min(\max(x,0),L)\). Summing (3) over all preceding Fibonacci blocks, using \(\sum_{i=3}^{j-1}F_i/F_j\to\varphi\), and counting the current partial block yields the complete phase profile of ordinary empirical densities:
\[
\frac{|E_{q,\theta}\cap[1,N_j]|}{N_j}
\longrightarrow
R(s)=\frac{\varphi L+\operatorname{clip}(s-1-t_-;0,L)}s.
\tag{4}
\]
The accumulated errors remain \(o(F_j)\) because the Fibonacci scales grow geometrically. The function \(R\) is continuous, strictly decreases on \([1,1+t_-]\), increases on \([1+t_-,1+t_+]\), and decreases on \([1+t_+,\varphi]\): for the middle interval, the derivative has the sign of \(1+t_--\varphi L>0\), since \(L<u\) and \(\varphi u=1\). It follows that the global minimum and maximum of \(R\) are exactly the two boxed natural-density constants. They are distinct, and their full interval is realized by choosing \(N_j\sim sF_j\). This proves the natural-density classification for **all** cutoff sequences.

**5. Logarithmic-density summation.** The weighted count in each complete block has the limit
\[
\sum_{\substack{F_j-1\le n\le F_{j+1}-2\\n\in E_{q,\theta}}}\frac1n
\longrightarrow\int_{t_-}^{t_+}\frac{dt}{1+t}
=\log\frac{1+t_+}{1+t_-},
\tag{5}
\]
by (2), threshold transversality, and Riemann summation. The number of complete Fibonacci blocks up to \(N\) is \(\log N/\log\varphi+O(1)\), and the harmonic contribution of an incomplete block is uniformly bounded. Cesàro averaging of (5) gives the boxed logarithmic density. All assertions follow.

## Verification
The standalone standard-library program `verify.py` directly constructs up to \(F_{13}\) initial irrational-rotation points at 90-digit decimal precision, independently sorts their circular gaps, and checks the predicted multiplicities and Rényi deficits for nonconsecutive scales. It performs 45 high-precision independent orbit-gap cases, 180 finite entropy comparisons, and 8 large-cutoff tests of the two extremal density formulas for four positive Rényi orders. Reproduce from the extracted package directory with `python3 verify.py`. These are finite diagnostics; the infinite density limits are proved in Steps 2–5, not inferred from a finite table.

For the Shannon order \(q=1\), the endpoint deficit is \(0.0247010166\ldots\) nats and the maximal deficit is \(0.0535540014\ldots\). Choosing their midpoint as threshold gives \(t_-=0.0783435867\ldots\), \(t_+=0.5150096656\ldots\), natural lower and upper densities \(0.6552091245\ldots\) and \(0.7545870249\ldots\), and logarithmic density \(0.7065405573\ldots\). This illustrates that the predicted separation is macroscopic, not a numerical rounding artifact.

## Relationship to prior work
The Fibonacci rotation coding, its unique invariant measure and elementary dynamical structure are classical and are used in [1]. The relation between Sturmian factor frequencies and rotation gaps and the complete three-distance multiplicity theorem are established, not new, results presented explicitly in [2, Section 6.2, Theorem 6.5]. These facts **do** determine the finite-block frequency table; no new frequency theorem is claimed. The new quantitative object is the arithmetic distribution, over the word-length parameter, of the events that a Rényi entropy deficit crosses an arbitrary nontrivial threshold. The two sharp and different ordinary-density limits, full continuous accumulation interval, and exact logarithmic density require analyzing all Fibonacci renormalization scales and counting threshold crossings within each. The earlier results and the nearby finite-type-cover entropy result [4] do not give this length-density classification. The canonical finite-type cover topological entropy in [4] is different from \(H_q(n)\), which is an entropy of actual invariant-measure word frequencies.

## Limitations
The theorem is for the Fibonacci irrational slope, the canonical Sturmian invariant measure, fixed Rényi order \(q>0\) and thresholds strictly between the stated endpoints. It does not cover arbitrary irrational rotations, threshold equalities, or finite-sample rates beyond the stated asymptotics. The input gap-frequency formula belongs to classical prior work; the contribution is the joint arithmetic-density classification built on it. An earlier unindexed specialization of three-distance entropy statistics could contain the same density result. No independent historical-priority or proof audit is claimed.

## References
[1] Henk Bruin and Renaud Leplaideur, *Renormalization, freezing phase transitions and Fibonacci quasicrystals*, arXiv:1309.7934v1 (first publicly posted 2013-09-30), Sections 1 and 2.1, https://arxiv.org/html/1309.7934v1.

[2] Valérie Berthé, *Sequences of Low Complexity: Automatic and Sturmian Sequences*, author's openly available survey, Sections 2.2, 4.2 and 6.2, especially Theorem 6.5, https://www.irif.fr/~berthe/Articles/chili.pdf (first-public date not independently established).

[3] Andrew Carey and Joseph P. Clampitt, *Partitioned Factors in Christoffel and Sturmian Words*, arXiv:1804.08724 (2018), particularly the gap-frequency correspondence, https://arxiv.org/pdf/1804.08724.

[4] *A Fibonacci entropy staircase and its full scaled accumulation interval*, public published-finding corpus mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-fibonacci-entropy-staircase-and-its-full-scaled-accumulation-i--be7c0c99809f (the title's entropy refers to canonical finite-type covers, not the invariant-measure Rényi block entropy here).
