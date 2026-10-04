# Exactly two connected components for the unitary divisor range at \(t=-2\)
## Finding
Let \(\sigma_t^*\) denote the unitary divisor function. Thus, for a prime \(p\) and an integer \(a\geq1\),
\[
\sigma_t^*(p^a)=1+p^{at}.
\]
For
\[
\mathcal R=\overline{\sigma_{-2}^*(\mathbb N)},
\]
one has the exact identity
\[
\mathcal R=\left[1,\frac{41}{3\pi^2}\right]\cup\left[\frac{25}{18},\frac{15}{\pi^2}\right].
\]
The intervals are disjoint. Therefore the closure has exactly two connected components. In the notation used for the component-count problem, \(\mathcal N^*(-2)=2\), so \(-2\in\mathcal E_2^*\).

## Assumptions and scope
The closure is taken in \(\mathbb R\). A prime may be absent from an integer; for bookkeeping this contributes the factor \(1\). If a prime \(p\) occurs with exponent \(a\geq1\), it contributes \(1+p^{-2a}\). Only the parameter \(t=-2\) is classified here; no monotonicity in \(t\) and no classification of other component counts is claimed.

Write \(p_j\) for the \(j\)-th prime and, for \(m\geq1\), let \(\mathcal T_m\) be the closure of products built only from primes \(p_m,p_{m+1},\ldots\). Defant's greedy interval argument applies verbatim to such a tail: if
\[
\frac{p_j^4+p_j^2}{p_j^4+1}\leq\prod_{i>j}(1+p_i^{-2})
\]
for every \(j\geq m\), then
\[
\mathcal T_m=\left[1,\prod_{i\geq m}(1+p_i^{-2})\right].
\]
The proof depends only on the available prime factors from index \(m\) onward, so deleting finitely many earlier primes does not alter the argument.

## Proof
First consider the tail beginning with \(5=p_3\). Put
\[
P_j=\prod_{i\leq j}(1+p_i^{-2}),\qquad
L_j=\frac{p_j^4+p_j^2}{p_j^4+1},\qquad
F_j=P_jL_j.
\]
The required tail inequality is equivalent to
\[
F_j\leq\prod_p(1+p^{-2})=\frac{\zeta(2)}{\zeta(4)}=\frac{15}{\pi^2}.
\]
For \(j\in\{3,4,6,9\}\), direct rational arithmetic gives
\[
\pi^2<\frac{484}{49}<\frac{15}{F_j}.
\]
The corresponding exact right-hand bounds are
\[
\frac{8451}{845},\quad \frac{32427}{3250},\quad
\frac{2286145323}{229177000},\quad
\frac{1787012500255983}{179882180200000},
\]
respectively. For all other indices relevant to this tail, the prime-ratio lemma used in the published proof gives
\[
\frac{p_{j+1}}{p_j}<2^{1/3}.
\]
The algebra in the same proof then yields \(F_{j+1}>F_j\). Hence \(F_5<F_6\), \(F_7<F_8<F_9\), and \((F_j)_{j\geq10}\) is increasing to \(15/\pi^2\). Thus every tail inequality for \(j\geq3\) holds. The tail criterion gives
\[
\mathcal T_3=[1,R],\qquad
R=\prod_{p\geq5}(1+p^{-2})
=\frac{15/\pi^2}{(1+2^{-2})(1+3^{-2})}
=\frac{54}{5\pi^2}.
\]

Now adjoin the prime \(3\). Set \(c_a=1+3^{-2a}\). Since \(c_2<R\), all intervals \(c_a[1,R]\) with \(a\geq2\), together with the interval obtained by omitting \(3\), merge into
\[
A=\left[1,c_2R\right]=\left[1,\frac{164}{15\pi^2}\right].
\]
The exponent-one interval is
\[
B=c_1[1,R]=\left[\frac{10}{9},\frac{12}{\pi^2}\right].
\]
The classical Archimedean bounds
\[
\frac{223}{71}<\pi<\frac{22}{7}
\]
show both \(c_2<R\) and
\[
\frac{164}{15\pi^2}<\frac{10}{9},
\]
so \(\mathcal T_2=A\cup B\), with a genuine gap between these two intervals.

Finally adjoin the prime \(2\). Let \(d_a=1+2^{-2a}=1+4^{-a}\). For every \(a\geq2\), the intervals \(d_aA\) begin inside \(A\), and their right endpoints are no larger than the right endpoint of \(d_2A\), which lies below the right endpoint of \(B\). The interval \(d_4A\) reaches past the left endpoint of \(B\); explicitly,
\[
\frac{257}{256}\frac{164}{15\pi^2}>\frac{10}{9},
\]
where \(\pi<22/7\) is enough. Thus \(A\), all \(d_aA\) with \(a\geq2\), and \(B\) form one connected block.

Likewise all \(d_aB\) with \(a\geq2\) overlap that block, and the largest right endpoint among them is
\[
d_2\frac{12}{\pi^2}=\frac{51}{4\pi^2}.
\]
The interval
\[
d_1A=\left[\frac54,\frac{41}{3\pi^2}\right]
\]
overlaps this block because \(5/4<51/(4\pi^2)\). Consequently all cases except exponent one at both \(2\) and \(3\) merge into
\[
\left[1,\frac{41}{3\pi^2}\right].
\]
The remaining case is
\[
d_1B=\left[\frac{25}{18},\frac{15}{\pi^2}\right].
\]
Finally,
\[
\frac{41}{3\pi^2}<\frac{25}{18}
\]
is equivalent to \(\pi^2>246/25\), which follows from \(223/71<\pi\). Hence the two displayed intervals are disjoint, and they exhaust the closure.

## Verification
The accompanying verifier checks, with exact rational arithmetic, the four fixed tail inequalities after replacing \(\pi^2\) by the rigorous upper bound \((22/7)^2\), all interval-overlap and interval-separation inequalities, and the finite prime-ratio part of the published lemma through index \(3099\). It also prints the decimal endpoints
\[
1.3847228431\ldots<1.3888888888\ldots
\]
of the unique gap. The finite prime-ratio check is corroborative for the published lemma; the proof above uses the published analytic argument for its infinite tail.

## Relationship to prior work
Defant's paper introduces the unitary divisor range, proves that its closure is connected exactly up to a critical parameter \(\eta^*\approx1.9742550\), and then asks for the sets of parameters giving each possible number of connected components. At \(t=-2\), that theorem says only that the closure is disconnected. The paper's proof contains the tail inequalities needed here but does not state the exact closure or the number of components at \(t=-2\). Its later published version still presents the component-count problem as a future direction.

Subsequent papers by Zubrilina and by Achenjang--Berger study connected components and gaps for the ordinary divisor function \(\sigma_{-r}\), not for the unitary divisor function \(\sigma_{-r}^*\). Their theorems therefore do not imply the two-interval identity proved here.

## Limitations
This result is a single exact parameter value. It does not prove that the component count for unitary divisor ranges is monotone, does not determine an interval of parameters around \(-2\) with two components, and does not classify any putative unitary Zubrilina numbers. The originality assessment is based on searches of the primary paper, its updated published version, later ordinary-divisor component papers, and semantic/bibliographic searches; literature not indexed by those routes remains a residual risk.

## References
1. C. Defant, *Ranges of Unitary Divisor Functions*, arXiv:1507.02654, first public version 2015-07-09; later published in *Integers* 18 (2018), A15.
2. J. Nagura, *On the interval containing at least one prime number*, Proc. Japan Acad. 28 (1952), 177--181.
3. N. Zubrilina, *On the Number of Connected Components of Ranges of Divisor Functions*, arXiv:1711.02871.
4. N. Achenjang and A. Berger, *On Gaps in the Closures of Images of Divisor Functions*, arXiv:1808.07550.
