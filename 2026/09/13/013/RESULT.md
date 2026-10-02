# No single-step whole-layer advance for thick slabs in strict-majority bootstrap on high-dimensional tori

## Context

Consider strict-majority bootstrap percolation on the torus \(T=(\mathbb Z/n\mathbb Z)^d\), where each vertex has degree \(2d\) and a healthy vertex becomes infected once at least \(d+1\) neighbours are infected. Condition on the thickness-2 slab
\[
S=\{x:x_d\in\{0,1\}\}
\]
being fully infected, while all vertices outside \(S\) are initially infected independently with probability
\[
p=\frac12+\frac1{\sqrt d}.
\]
Let \(L=\{x:x_d=2\}\) be the adjacent layer.

The result below addresses only *simultaneous one-update advance* of the whole layer. It does not rule out multi-round cleanup and it does not prove the global critical-window law.

## Result

**Theorem.** For every \(d\ge16\) and \(n\ge20\), set
\[
c=\frac{e^{-8}}4,\qquad m=\lfloor n/4\rfloor^{d-1}.
\]
Then
\[
\Pr(L\text{ is fully infected after one update}\mid S\text{ infected})
\le \left(1-\frac{c}{\sqrt d}\right)^m
\le \exp\!\left(-\frac{cm}{\sqrt d}\right).
\]
Moreover \(m\ge(n/8)^{d-1}\). Hence along
\[
d(n)=\lfloor(\log\log n)^3\rfloor
\]
the one-update whole-layer success probability tends to zero super-exponentially fast.

## Proof

Fix \(v=(y,2)\in L\). Exactly one neighbour of \(v\), namely \((y,1)\), lies in the conditioned infected slab. Let \(N(v)\) be the other \(2d-1\) neighbours: the \(2(d-1)\) neighbours within \(L\) together with \((y,3)\).

If \(v\) is initially healthy, it can become infected in the first update only if at least \(d\) vertices of \(N(v)\) are initially infected. Define
\[
F_v=\{\#(N(v)\cap A_0)\le d-1\},
\qquad
H_v=\{v\notin A_0\}\cap F_v.
\]
The event \(H_v\) is therefore a genuine one-update failure at \(v\).

For \(F_v\),
\[
\Pr(F_v)\ge
\binom{2d-1}{d-1}p^{d-1}(1-p)^d.
\]
Write \(p=(1+\delta)/2\) with \(\delta=2/\sqrt d\). The central-binomial estimate
\[
\binom{2d}{d}4^{-d}\ge\frac1{2\sqrt d}
\]
gives
\[
\binom{2d-1}{d-1}\ge\frac{4^d}{4\sqrt d}.
\]
Consequently
\[
\Pr(F_v)
\ge
\frac1{2\sqrt d}(1-\delta^2)^{d-1}(1-\delta).
\]
For \(d\ge16\), \(1-\delta\ge1/2\), and
\[
(d-1)\log(1-4/d)\ge-6,
\]
so
\[
\Pr(F_v)\ge\frac{e^{-6}}{4\sqrt d}.
\]

The initially healthy state of \(v\) is independent of the initial states on \(N(v)\). Also, for \(d\ge16\),
\[
1-p=\frac12-\frac1{\sqrt d}\ge\frac14.
\]
Thus
\[
\Pr(H_v)
=(1-p)\Pr(F_v)
\ge\frac{e^{-6}}{16\sqrt d}
\ge\frac{e^{-8}}{4\sqrt d}
=\frac{c}{\sqrt d},
\]
where the penultimate inequality is equivalent to \(e^2\ge4\).

Now take the spacing-4 set
\[
Y=\{0,4,8,\ldots,4(\lfloor n/4\rfloor-1)\}^{d-1}
\]
inside the first \(d-1\) coordinates and sample the vertices \((y,2)\), \(y\in Y\). Their closed radius-1 dependency sets \(\{v\}\cup N(v)\) are pairwise disjoint, so the events \(H_v\) are independent. If the whole layer is infected after one update, none of these \(m=|Y|\) events can occur. Therefore
\[
\Pr(L\text{ fully infected after one update}\mid S\text{ infected})
\le\prod_{y\in Y}(1-\Pr(H_{(y,2)}))
\le\left(1-\frac{c}{\sqrt d}\right)^m.
\]
The exponential bound follows from \(1-x\le e^{-x}\). Since \(\lfloor n/4\rfloor\ge n/8\) for \(n\ge8\), the stated lower bound on \(m\) follows.

## Reproducibility

`artifacts/emergent_check.py` recomputes the binomial-tail values, the central-binomial bound, and the growth scale of the packing exponent. The analytic proof above supplies the essential initially-healthy factor that was omitted from the earlier proof text.

## Limitations

This theorem refutes only a simultaneous one-update whole-layer mechanism. Multi-round bootstrap cleanup remains possible, and neither side of the full near-one-half window law is proved here.

## References

- J. Balogh, B. Bollobás, R. Morris, *Majority bootstrap percolation on the hypercube*, arXiv:math/0702373.
- M. Collares, J. Erde, A. Geisler, M. Kang, *Universal behaviour of majority bootstrap percolation on high-dimensional geometric graphs*, arXiv:2406.17486.
