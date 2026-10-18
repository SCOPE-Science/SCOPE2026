# Two endpoint scales for an absorbed pure-birth semigroup

## Finding

Let \(n\ge1\), let \(Q_n\) be the generator of a uniform-rate pure-birth chain on \(\{0,1,\dots,n\}\), stopped at \(n\), and let \(T_n(t)=e^{tQ_n}\). With counting-measure endpoint norms and \(p_k(t)=e^{-t}t^k/k!\), put \(F_{n-1}(t)=\sum_{k=0}^{n-1}p_k(t)\) and \(m_n(t)=\min\{\lfloor t\rfloor,n-1\}\). For every \(t>0\), the *exact* derivative norms are
\[
\|Q_nT_n(t)\|_{\ell^\infty\to\ell^\infty}=2p_{m_n(t)}(t)
\]
and
\[
\|Q_nT_n(t)\|_{\ell^1\to\ell^1}
 =\max\{F_{n-1}(t),B_n(t)\},\qquad
B_n(t)=\begin{cases}
2p_{\lfloor t\rfloor}(t)-p_{n-1}(t),&0<t<n-1,\\
p_{n-1}(t),&t\ge n-1.
\end{cases}
\]
(The first branch is empty when \(n=1\).) In particular, writing \(M_{p,n}=\sup_{t>0}t\|Q_nT_n(t)\|_{\ell^p\to\ell^p}\), one has the *exact* sharp constant
\[
M_{\infty,n}=\frac{2n^{n+1}e^{-n}}{n!}
=\sqrt{\frac{2n}{\pi}}\left(1-\frac1{12n}+O(n^{-2})\right),
\]
with the unique maximizing time \(t=n\). For every \(n\ge1\), the function \(tF_{n-1}(t)\) has a unique maximizer \(r_n>0\), characterized by
\[
F_{n-1}(r_n)=r_np_{n-1}(r_n).
\]
For all sufficiently large \(n\), \(M_{1,n}=r_nF_{n-1}(r_n)\), and its global maximizing time is uniquely \(r_n\). Its localization and sharp growth are
\[
r_n=n-\sqrt{n\log n}\,(1+o(1)),\qquad
M_{1,n}=n-\sqrt{n\log n}\,(1+o(1)).
\]
Consequently,
\[
\frac{M_{1,n}}{M_{\infty,n}}\sim\sqrt{\frac{\pi n}{2}}.
\]
All these assertions hold for real and complex \(\ell^p\) spaces. The spectrum of each generator is precisely \(\{-1,0\}\): eigenvalue \(-1\) has algebraic multiplicity \(n\), while \(0\) is simple. Thus bounded spectral location does not prevent the strikingly different growth of the two time-weighted endpoint constants in this nonnormal positive-semigroup family.

## Assumptions and scope

The norms on \(\mathbb C^{n+1}\) or \(\mathbb R^{n+1}\) use the **unweighted counting measure**. For \(0\le i<n\) let \((Q_nf)(i)=f(i+1)-f(i)\), and set \((Q_nf)(n)=0\). The Markov semigroup is positive, preserves constants, and is a contraction on \(\ell^\infty\). No irreducibility or reversibility is assumed. The generating rate is one; replacing it by any \(\lambda>0\) rescales time and leaves \(M_{p,n}\) unchanged. The theorem is for all integer \(n\ge1\), all \(t>0\), and only the two endpoint exponents. It makes no claim about interior \(p\).

## Proof

**1. Stopped-Poisson kernel and its derivative.** For \(0\le i<n\) and \(0\le k<n-i\), the transition probability from \(i\) to \(i+k\) is \(p_k(t)\), and that from \(i\) to the absorbing state \(n\) is \(1-\sum_{k=0}^{n-i-1}p_k(t)\). The absorbing row is the coordinate mass at \(n\). This follows either by the exponential series or by stopping a unit-rate Poisson counting process. Set \(p_{-1}=0\). Then \(p_k'=p_{k-1}-p_k\), and the derivative of the absorbing probability is \(p_{n-i-1}\).

**2. Row sums.** Put \(r=n-i\). The nonterminal entries of the derivative row are \(p_k'\), \(0\le k<r\), while the terminal entry is \(p_{r-1}>0\). For fixed \(t\), the Poisson probabilities increase through index \(\lfloor t\rfloor\) and decrease afterward (with harmless ties at integral \(t\)). Hence the total negative mass of this zero-sum row is \(p_{\min(\lfloor t\rfloor,r-1)}\). Its absolute row sum is twice this mass. Maximizing over \(r\in\{1,\ldots,n\}\) proves the exact \(\ell^\infty\) norm.

**3. Column sums.** The derivative of the terminal column is nonnegative in each nonabsorbing row and has sum \(F_{n-1}(t)\). For a nonterminal column \(j\), the nonzero entries are \(p_0',p_1',\dots,p_j'\), so its absolute sum is \(p_j\) when \(j\le\lfloor t\rfloor\), and \(2p_{\lfloor t\rfloor}-p_j\) otherwise. Maximizing over \(0\le j<n\) gives \(B_n(t)\). The maximum of terminal and nonterminal column sums proves the exact \(\ell^1\) norm. Absolute row/column sums are operator norms on both real and complex coordinate spaces.

**4. Exact time optimization at \(\ell^\infty\).** On every interval \(k\le t<k+1\) with \(k<n-1\), the quantity \(tp_k(t)\) is strictly increasing because its derivative has the sign of \(k+1-t\). At integer interfaces the two adjacent Poisson masses agree. For \(t\ge n-1\), the expression is \(tp_{n-1}(t)\), which has its unique maximum at \(t=n\). Evaluating there gives \(2n^{n+1}e^{-n}/n!\). Stirling's expansion supplies the displayed relative \(1/n\) correction.

**5. The leading \(\ell^1\) optimizer.** Differentiate \(H_n(t)=tF_{n-1}(t)\):
\[
H_n'(t)=F_{n-1}(t)-tp_{n-1}(t).
\]
The ratio \(F_{n-1}(t)/(tp_{n-1}(t))=\sum_{k=0}^{n-1}(n-1)!/(k!t^{n-k})\) decreases strictly from infinity to zero. Hence \(H_n\) has exactly one global maximizer, \(r_n\). Uniform Poisson mode estimates obtained from Stirling imply \(\sup_{t>0}tB_n(t)=O(\sqrt n)\): for \(t<n-1\), use \(tB_n\le2t\,p_{\lfloor t\rfloor}=O(\sqrt{t+1})\), and for \(t\ge n-1\), maximize \(tp_{n-1}\) at \(n\). In contrast \(\max H_n=n(1-o(1))\), as shown next. Thus eventually \(\sup tB_n<\max H_n\), establishing both the exact \(M_{1,n}\) representation and uniqueness of its maximizing time for all sufficiently large \(n\).

**6. Moderate-deviation boundary layer.** Fix \(c>0\) and set \(t_c=n-c\sqrt{n\log n}\), for sufficiently large \(n\). Uniform Stirling expansion in this range yields
\[
t_cp_{n-1}(t_c)=\frac{n^{(1-c^2)/2}}{\sqrt{2\pi}}(1+o(1)),
\qquad F_{n-1}(t_c)\longrightarrow1.
\]
For the second limit, the Poisson upper-tail Chernoff bound suffices. For \(c>1\), \(H_n'(t_c)>0\) eventually; for \(0<c<1\), \(H_n'(t_c)<0\) eventually. The unique root therefore obeys \((n-r_n)/\sqrt{n\log n}\to1\). At the root, \(p_n(r_n)=(r_n/n)p_{n-1}(r_n)=F_{n-1}(r_n)/n\). Since \(r_n<n\) for large \(n\), the Poisson upper tail satisfies
\[
1-F_{n-1}(r_n)=\sum_{j=n}^{\infty}p_j(r_n)
\le\frac{p_n(r_n)}{1-r_n/(n+1)}
\le\frac{n+1}{n(n+1-r_n)}.
\]
Consequently \(n[1-F_{n-1}(r_n)]=O(\sqrt{n/\log n})=o(\sqrt{n\log n})\), and \(r_nF_{n-1}(r_n)=n-\sqrt{n\log n}(1+o(1))\). This completes the proof.

## Verification

The standalone `checker.py` reproduces both exact endpoint formulas by an independently evaluated finite-matrix exponential and direct absolute row/column sums, with \(n\in\{1,\ldots,10\}\) and multiple fixed times. It additionally checks the sharp \(\ell^\infty\) envelope over finite sample grids and numerically locates roots of \(F_{n-1}(t)=tp_{n-1}(t)\) for several sizes. The script uses only the Python 3 standard library and prints its finite comparison count upon successful completion. Numeric testing supports but does **not** prove the theorem; the proof above handles all \(n\) and \(t\) and the asymptotic regimes.

## Relationship to prior work

The stopped Poisson kernel and unimodality of Poisson masses are classical facts, not claimed as discoveries. Borichev and Tomilov treat abstract resolvent-controlled semigroup decay; their hypotheses, targets, and orbit-decay conclusions do not provide exact dual endpoint derivative norms for these absorbing nonnormal generators. Orsingher and Polito analyze fractional linear birth–death state distributions and subordination, rather than sharp operator norms for finite constant-rate absorbed pure-birth generators. Chen and Saloff-Coste study mixing times and gaps of irreducible birth–death chains, unlike this reducible absorbing chain. The distinctive assertion here is the paired **sharp time-optimized operator-norm law**, including the \(\ell^1\) moderate-deviation maximizing-time correction and the contrasting \(\ell^\infty\) square-root scale.

## Limitations

The theorem does not supply sharp constants for \(1<p<\infty\). The \(\ell^1\) optimizer identification is asserted for **all sufficiently large** \(n\), not for all small sizes. No claim is made that Poisson probabilities, their modes, Stirling asymptotics, or the bare matrix-exponential formula are original. Exhaustive historical priority and independent verification remain unperformed; equivalent descriptions under phase-type distributions, stopped-Poisson total variation, or triangular Markov semigroups remain a bibliographic risk. An older absorption-process reference was identifiable by abstract but its full text was inaccessible, leaving an explicit gap in the literature comparison.

## References

1. A. Borichev and Y. Tomilov, *Optimal polynomial decay of functions and operator semigroups*, arXiv:0910.0859v1 (posted 2009-10-05), https://arxiv.org/html/0910.0859v1.
2. E. Orsingher and F. Polito, *On a fractional linear birth–death process*, arXiv:1102.1620v1 (posted 2011-02-08), https://arxiv.org/abs/1102.1620.
3. G.-Y. Chen and L. Saloff-Coste, *On the mixing time and spectral gap for birth and death chains*, arXiv:1304.4346v1 (posted 2013-04-16), https://arxiv.org/html/1304.4346v1.
