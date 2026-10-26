# Atomic stationary laws without pointwise average expansion in a random dyadic circle system

## Finding
Consider the circle maps \(D(x)=2x\pmod 1\) and
\[
B(x)=\begin{cases}
 x/2+1/4,&0\le x<1/2,\\
 2x-1/2,&1/2\le x<3/4,\\
 x-3/4,&3/4\le x<1.
\end{cases}
\]
At each step apply \(D\) independently with probability \(p\) and \(B\) with probability \(1-p\). For every \(2/5\le p<1\), there exists exactly one stationary probability supported on the countable dyadic set \(\mathcal D=\mathbb Z[1/2]/\mathbb Z\). It has a finite exponential denominator-depth moment: for some \(s>1\), \(\sum_{x\in\mathcal D}s^{G(x)}\nu_p(\{x\})<\infty\), where \(G(0)=0\) and \(G(a/2^n)=n\) for odd \(a\). In particular, this holds on \(2/5\le p\le1/2\), although on the open semicircle \((0,1/2)\) the expected logarithmic derivative is \((2p-1)\log2\le0\). Thus strict pointwise expansion on average is not necessary for an atomic stationary law with an exponentially decaying denominator-depth tail in this example.

## Assumptions and scope
The maps are interpreted as continuous circle maps, so the values at \(3/4\) and the terminal endpoint agree modulo one. The state space for the uniqueness assertion is \(\mathcal D\) with its countable discrete topology. The theorem does not assert uniqueness among *all* stationary probabilities on the circle, nor that the dyadic stationary law is physical for Lebesgue-generic starts. The parameter cutoff \(2/5\) is a rigorously certified sufficient bound, not a claimed optimal threshold. The natural stochastic update acts on dyadics because both maps preserve that set.

## Proof
Write a positive dyadic \(x\) in its terminating binary expansion of minimal length \(n=G(x)\). If its first four bits are \(b_1b_2b_3b_4\), then under \(D\) the first three bits become \(b_2b_3b_4\) and depth falls by one. Under \(B\), the binary rewriting and depth change for \(n\ge4\) are exactly
\[
0b_2b_3b_4\longmapsto 01b_2b_3b_4\quad(+1),\qquad
10b_3b_4\longmapsto 1b_3b_4\quad(-1),\qquad
11b_3b_4\longmapsto 00b_3b_4\quad(0).
\]
These follow respectively by adding \(1/4\) after division by two, subtracting \(1/2\) after doubling, and subtracting \(3/4\). For depth at least four no branch boundary creates additional cancellation at the terminating binary digit. In every case the first three output bits are fully determined by four input bits.

Put \(s=51/50\), \(\lambda=3999/4000\), and define the eight strictly positive weights \(a_{000},a_{001},\ldots,a_{111}\), in lexicographic order, by
\[
\frac1{100000}(101275,101199,100542,101080,97952,98566,99446,99939).
\]
For every dyadic with \(G(x)\ge4\), set \(V(x)=s^{G(x)}a_{b_1b_2b_3}\); for depth less than four use the same formula with the terminating binary word padded with zeros to three bits. This defines a positive proper function on the countable dyadic set: the sublevels \(\{V\le R\}\) are finite because \(s>1\) and the eight weights have a positive minimum.

For each of the sixteen possible four-bit words \(w\), let \(i\) be its first-three-bit index, \(j\) the index of the last three bits, and \(k\) the index of the three-bit prefix after the above \(B\)-rewrite. Let \(\Delta(w)\in\{-1,0,1\}\) be the corresponding depth change. The finite inequalities
\[
\lambda a_i-\frac{p}{s}a_j-(1-p)s^{\Delta(w)}a_k>0
\]
hold for all sixteen words at **both** \(p=2/5\) and \(p=1/2\). Direct exact rational enumeration gives respective minimum slacks \(3409/170000000\) and \(268567/10200000000\). Both are positive, and the displayed left side is affine in \(p\), so the inequality holds throughout \([2/5,1/2]\). Multiplying by \(s^{G(x)}\) yields \(P_pV(x)\le\lambda V(x)\) for every \(G(x)\ge4\).

Let \(K=\{x:G(x)<4\}\), a finite set. Since the maps take dyadics to dyadics, the preceding inequality and finiteness of \(K\) yield \(P_pV\le\lambda V+C\mathbf 1_K\) for some finite \(C\), uniformly for fixed \(p\in[2/5,1/2]\). Hence from \(x_0=0\), \(\mathbb E V(X_n)\le\lambda^nV(0)+C/(1-\lambda)\). The Cesàro averages of its laws are tight on the countable discrete space because \(V\) is proper. Every weak accumulation point is stationary (the one-step telescoping identity gives stationarity), and Fatou's lemma gives it a finite \(V\)-moment, hence a finite \(s\)-exponential denominator-depth moment.

For uniqueness, every state \(x\in\mathcal D\) reaches zero with positive probability after \(G(x)\) consecutive applications of \(D\). Therefore any closed recurrent communicating class contains zero, and there is at most one such class. Existence of a stationary probability forces a positive recurrent class. Thus the dyadic stationary probability is unique. For \(p>1/2\), Theorem 3.5 of the cited Goverse--Kleptsyn paper applies: the pointwise expected log derivative is positive on all three affine branches, and their proof gives recurrence with an exponential depth Lyapunov function. In the limit \(p=1\), \(\delta_0\) is the unique dyadic stationary law; the assertion here excludes that endpoint only to keep both probabilities nonzero.

Finally, on \((0,1/2)\), the slopes of \(D\) and \(B\) are \(2\) and \(1/2\), respectively. Therefore their expected logarithmic slope is \(p\log2+(1-p)\log(1/2)=(2p-1)\log2\), which is nonpositive for all newly certified parameters. This proves the advertised failure of necessity of strict pointwise average expansion.

## Verification
The companion `CHECK.py` performs all \(32\) exact four-bit, two-endpoint rational inequalities; it also directly checks \(504\) nonzero dyadic inputs of depths four through nine against the original rational maps and their binary rewrite rules. `CHECK_OUTPUT.txt` records the execution. The finite certificate proves a uniform inequality for **all** depths because the four-bit rewrite identity is exact, not because a finite list of states was sampled. The Markov-chain existence and uniqueness assertions follow from the analytical Foster and accessibility argument above, not from simulation.

## Relationship to prior work
Goverse and Kleptsyn (arXiv:2607.11421v2, Example 3.1 and Theorem 3.5) introduce exactly these maps and establish an atomic stationary probability under the sufficient condition \(p>1/2\), coming from strictly positive expected logarithmic slope at every non-dyadic point. Their Lemma 3.2 already proves that the maps have no common invariant probability. The present finite-prefix Lyapunov function certifies the genuinely non-average-expanding interval \(2/5\le p\le1/2\) instead. The general Foster--Lyapunov recurrence principle is classical and is used with attribution; the new content is the explicit model-specific rational finite-prefix certificate and consequent sign-changing parameter extension. Neither existence in this additional interval nor the certificate is stated in the inspected source.

## Limitations
The lower cutoff is sufficient, not proved sharp; nothing is asserted about \(0<p<2/5\). The stationary law need not be globally unique among measures on the entire circle. Physicality for non-dyadic starts, convergence rates in circle metrics, and smooth analogues are not established. A more general published recurrence criterion might imply the qualitative extension, and independent historical-priority review is still needed.

## References
1. Vincent P. H. Goverse and Victor Kleptsyn, *Atomic physical measures for non-invertible random dynamical systems*, arXiv:2607.11421v2 (first public version July 13, 2026), especially Example 3.1, Theorem 3.5, and Section 3.3; https://arxiv.org/html/2607.11421v2.
2. Classical countable-state Foster--Lyapunov positive recurrence and tightness arguments; the source above cites a standard theorem in its Section 3.3. The complete compactness proof needed here is included above.
