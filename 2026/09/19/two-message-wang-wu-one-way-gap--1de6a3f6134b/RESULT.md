# Two messages suffice for the Wang--Wu separation, while one message costs polynomially more

## Statement

Wang and Wu construct a family of total Boolean functions
\[
F_n:\{0,1\}^n\times\{0,1\}^n\to\{0,1\}
\]
with public-coin randomized communication \(O(\log n\log\log n)\) and with every monochromatic rectangle of density at most \(2^{-n^{\Omega(1)}}\). Their stated protocol is presented as three transmissions: Alice sends a sampling sketch, Bob returns the estimated cheat-sheet address, and Alice sends her fully linear-PCP shares for the selected cell.

For this same family, let \(R^{[2]}_{\rm pub}(F_n)\) denote the minimum public-coin cost of a protocol using at most two messages, and let \(R^{A\to B}_{\rm pub,1}(F_n)\) and \(R^{B\to A}_{\rm pub,1}(F_n)\) denote the two directional one-way complexities.

**Theorem.** For the Wang--Wu family,
\[
R^{[2]}_{\rm pub}(F_n)=O(\log n\log\log n),
\]
while
\[
R^{A\to B}_{\rm pub,1}(F_n),
\ R^{B\to A}_{\rm pub,1}(F_n)
=
\Omega\!\left(\frac{n^{1/3}}{(\log n)^{2/3}}\right).
\]
Consequently the function has a polynomial one-message/two-message gap. In particular, if \(\mathsf{BPP}[2]\) denotes total function families with polylogarithmic-cost public-coin protocols using at most two messages, then the Wang--Wu lower bound against adaptive \(\mathsf{NP}\) queries already gives
\[
\mathsf{BPP}[2]\not\subseteq \mathsf{P}^{\mathsf{NP}}
\]
in communication complexity.

The two-message upper bound preserves the source paper's \(O(\log n\log\log n)\) communication cost and its error guarantee; the one-way lower bound is an exact embedding of the standard INDEX problem into the same total function.

## The Wang--Wu function

Fix \(k\ge 12\), put \(m=2^k\), and let
\[
d=k\big(m(m+3)+1\big).
\]
Each party receives \(k\) length-\(m\) Gap-Hamming blocks together with a table of \(m\) certificate shares. Alice has
\[
(\mathbf x,\mathbf u),\qquad
\mathbf u=(\mathbf u_1,\ldots,\mathbf u_m),
\]
and Bob has
\[
(\mathbf y,\mathbf v),\qquad
\mathbf v=(\mathbf v_1,\ldots,\mathbf v_m).
\]
Writing \(\mathbf z=\mathbf x\oplus\mathbf y\), the \(k\) promised Gap-Hamming outputs select an address \(h\in[m]\). At that address the certificate is
\[
\mathbf c_h=\mathbf u_h\oplus\mathbf v_h.
\]
When every Gap-Hamming block is promised, the function equals
\[
\mathsf{Check}(\mathbf z,\mathbf c_h),
\]
and for each promised \(\mathbf z\) there is exactly one certificate \(\mathbf c^*(\mathbf z)\) accepted by \(\mathsf{Check}\).

The source paper's fully linear-PCP test works over \(\mathbb F_{2^{4k}}\). If \(p_A,p_B\) are the polynomials encoded by the two certificate shares, then for a public random \(r\) the global quantities used by the test are reconstructed from four local field elements per side:
\[
p(r)=p_A(r)+p_B(r),
\]
\[
f_{(\mathbf z,p)}(r)
=
f_{(\mathbf x,p_A)}(r)+f_{(\mathbf y,p_B)}(r)+f_{(\mathbf 0,p_0)}(r),
\]
\[
g_{(\mathbf z,p)}(r)
=
g_{(\mathbf x,p_A)}(r)+g_{(\mathbf y,p_B)}(r)+g_{(\mathbf 0,p_0)}(r),
\]
and
\[
p(\tau_d)=p_A(\tau_d)+p_B(\tau_d).
\]

## Two-message protocol

The source protocol can be reordered so that the party who learns the address also owns the PCP values that must be sent next.

Using the same public sample positions as Wang--Wu:

1. **Bob to Alice.** Bob sends the sampled bits
   \[
   \mathbf y_i(I_{i,j}),\qquad i\in[k],\ j\in[q],
   \]
   where \(q=\lceil 18\ln(6k)\rceil\). This costs \(kq=O(k\log k)\) bits.

2. Alice combines them with her sampled \(\mathbf x\)-bits, computes the estimated Gap-Hamming bits \(h_1,\ldots,h_k\), and hence the address \(h\). Using the public random field point \(r\), she evaluates her four local quantities for the selected share \(\mathbf u_h\).

3. **Alice to Bob.** Alice sends
   \[
   h_1,\ldots,h_k,
   \]
   together with
   \[
   p_A(r),\quad
   f_{(\mathbf x,p_A)}(r),\quad
   g_{(\mathbf x,p_A)}(r),\quad
   p_A(\tau_d).
   \]
   This costs \(k+16k=17k\) bits.

Bob now knows \(h\), selects \(\mathbf v_h\), computes the four corresponding local quantities from his input, reconstructs the same four global values as in the source protocol, and applies exactly the same acceptance test.

Thus the transcript contains only two messages and has total cost
\[
kq+17k=O(k\log k).
\]
Nothing in the probability analysis changes: the sampled differences have exactly the same distribution, the estimated address is exactly the same random variable as in the source proof, and conditioned on that address the same fully linear-PCP test is performed at the same public random field point. Hence the error is still \(<1/3\).

Since the input length satisfies \(k=\Theta(\log n)\), this gives
\[
R^{[2]}_{\rm pub}(F_n)=O(\log n\log\log n).
\]

The same observation may also be viewed as a symmetry correction: the function depends on the two inputs through XOR-shared base strings and XOR-shared certificates, so sampling from Bob first lets Alice combine the address response and her certificate-share response into one transmission.

## A one-way INDEX embedding

Let
\[
L=4k(2d-1)
\]
be the length of one certificate share, and fix any nonzero
\[
e\in\{0,1\}^{L}.
\]

Consider the standard INDEX problem: the sender has
\[
s=(s_1,\ldots,s_m)\in\{0,1\}^{m},
\]
the receiver has \(h\in[m]\), and the desired output is \(s_h\).

### Alice-to-Bob direction

Given \(s\), Alice forms a Wang--Wu input depending only on \(s\):
\[
\mathbf x=0^{km},
\qquad
\mathbf u_j=s_j e\quad(j\in[m]),
\]
where \(0e=0^L\) and \(1e=e\).

Given \(h\), write its address bits as \(h_1,\ldots,h_k\). Bob forms
\[
\mathbf y_i=
\begin{cases}
0^m,&h_i=0,\\
1^m,&h_i=1.
\end{cases}
\]
Every block is therefore a promised Gap-Hamming instance, and with \(\mathbf x=0\) the selected address is exactly \(h\).

Let
\[
\mathbf c^{*(h)}
\]
be the unique certificate accepted for this promised \(\mathbf z=\mathbf y\). Bob sets
\[
\mathbf v_h=\mathbf c^{*(h)}\oplus e
\]
and may set all unused entries \(\mathbf v_j\), \(j\ne h\), arbitrarily.

The selected certificate is then
\[
\mathbf u_h\oplus\mathbf v_h
=
\begin{cases}
\mathbf c^{*(h)}\oplus e,&s_h=0,\\
\mathbf c^{*(h)},&s_h=1.
\end{cases}
\]
Because \(e\ne0\) and the valid certificate is unique,
\[
F_n\big((\mathbf x,\mathbf u),(\mathbf y,\mathbf v)\big)=s_h.
\]

Thus INDEX on \(m\) bits is a restriction of \(F_n\) in which the sender's Wang--Wu input depends only on \(s\) and the receiver's input depends only on \(h\). Any public-coin Alice-to-Bob one-way protocol for \(F_n\) therefore gives one for \(\operatorname{INDEX}_m\) with the same communication.

### Reverse direction

The definition of \(F_n\) is symmetric under exchanging
\[
(\mathbf x,\mathbf u)\longleftrightarrow(\mathbf y,\mathbf v):
\]
both the base input and the selected certificate enter through XOR. Exchanging the parties in the restriction above therefore embeds INDEX in the Bob-to-Alice direction as well.

Hence
\[
R^{A\to B}_{\rm pub,1}(F_n),
\ R^{B\to A}_{\rm pub,1}(F_n)
\ge
R_{\rm pub,1}(\operatorname{INDEX}_m).
\]

## Self-contained one-way INDEX lower bound

For completeness, let \(S\) be uniform on \(\{0,1\}^{m}\), let \(H\) be uniform on \([m]\), and let \(R\) be the public randomness. Suppose a one-way protocol uses at most \(c\) bits and has error at most \(1/3\) on every input. Let \(M\) be the sender's message.

Binary Fano gives
\[
H(S_H\mid M,R,H)\le h_2(1/3),
\]
where \(h_2\) is binary entropy. Averaging over \(H\),
\[
\frac1m\sum_{i=1}^{m}H(S_i\mid M,R)\le h_2(1/3).
\]
Subadditivity therefore yields
\[
H(S\mid M,R)
\le
\sum_{i=1}^{m}H(S_i\mid M,R)
\le
m\,h_2(1/3).
\]
Since \(S\) is independent of \(R\),
\[
I(S;M\mid R)
=
m-H(S\mid M,R)
\ge
m(1-h_2(1/3)).
\]
But
\[
I(S;M\mid R)\le H(M\mid R)\le c.
\]
Consequently
\[
R_{\rm pub,1}(\operatorname{INDEX}_m)
\ge
(1-h_2(1/3))m
=
\Omega(m).
\]

## Converting the parameter to the final input length

The per-party input length in the Wang--Wu construction is
\[
n
=
km+4km(2d-1)
=
km(8d-3),
\]
with
\[
d=k(m(m+3)+1),\qquad m=2^k.
\]
For \(k\ge12\),
\[
n=\Theta(k^2m^3).
\]
Also \(k=\Theta(\log n)\). Therefore
\[
m
=
\Theta\!\left(\frac{n^{1/3}}{(\log n)^{2/3}}\right),
\]
and the INDEX restriction gives
\[
R^{A\to B}_{\rm pub,1}(F_n),
\ R^{B\to A}_{\rm pub,1}(F_n)
=
\Omega\!\left(\frac{n^{1/3}}{(\log n)^{2/3}}\right).
\]

Combining this with the two-message upper bound gives a polynomial communication collapse caused by one extra message:
\[
\widetilde\Omega(n^{1/3})
\quad\longrightarrow\quad
O(\log n\log\log n).
\]

## Consequences for the source separation

Wang--Wu prove for the same total functions that
\[
\operatorname{rect}(F_n)\le 2^{-n^{\Omega(1)}}
\]
and consequently
\[
\mathsf P^{\mathsf{NP}cc}(F_n)\ge n^{\Omega(1)}.
\]
The two-message protocol therefore strengthens the location of their witness inside randomized communication:
\[
F_n\in\mathsf{BPP}[2]
\qquad\text{but}\qquad
F_n\notin\mathsf P^{\mathsf{NP}}.
\]
Thus unrestricted interaction is not needed for their first total-function separation of randomized communication from adaptive \(\mathsf{NP}\)-query communication.

The source paper also proves a polynomial lower bound against adaptive exact \(\mathsf{RP}\) queries; the same witness therefore lies outside that model while retaining a two-message randomized protocol.

## Optional private-coin corollary

By the standard public-to-private randomness reduction of Newman, the public randomness can be reduced to \(O(\log n)\) shared random bits at an arbitrarily small constant increase in error. The first sender can sample the reduced public seed privately and include its index in the first message, so this conversion does not add a message.

After first decreasing the public protocol's error by a constant margin (for example, by increasing the sampling constant or by a constant number of parallel repetitions), the result is a private-coin two-message protocol of cost
\[
O(\log n\log\log n).
\]
This is a standard corollary rather than a new derandomization claim.

## Relation to prior work and originality boundary

The Wang--Wu paper proves the small-rectangle theorem, the \(\mathsf P^{\mathsf{NP}}\) and \(\mathsf P^{\mathsf{RP}}\) lower bounds, the fully linear-PCP decomposition, and the \(O(k\log k)\) randomized protocol. These are not claimed as new here.

The new claims are:

1. the same protocol can be arranged into two messages without increasing its asymptotic cost or changing its test;
2. the same total function contains \(\operatorname{INDEX}_m\) as an exact restriction in both one-way directions, giving the \(\widetilde\Omega(n^{1/3})\) one-way lower bound; and
3. therefore the Wang--Wu separation from \(\mathsf P^{\mathsf{NP}}\) already occurs inside the two-message randomized subclass.

The source manuscript was inspected in its statement of results, total-function definition, uniqueness lemma, fully linear-PCP test, and randomized protocol. The current v1 contains no occurrence of “one-way” or “round,” and does not state the two-message protocol or the INDEX restriction.

Gavinsky's preceding cheat-sheet work uses a two-message quantum protocol with fully linear PCPs, so the general idea of arranging a cheat-sheet verification around two messages is not claimed as new. The claim here is specific to the classical Wang--Wu witness and its matching one-way obstruction.

Targeted searches for the paper title and identifier together with “one-way,” “two-message,” “two-round,” “INDEX,” and related cheat-sheet terminology did not locate an earlier statement of these refinements. Because the motivating preprint is extremely recent and the two-message rearrangement is short once noticed, near-simultaneous observation or a subsequent author revision remains a material priority risk.

## Limitations

This result does not prove that the \(\widetilde\Omega(n^{1/3})\) one-way lower bound is tight. It does not improve the source paper's total communication bound, rectangle bound, or adaptive-query lower bounds. The one-way obstruction uses the uniqueness of the selected certificate and therefore is tailored to this totalization. The private-coin statement is only the standard Newman conversion.

## References

1. H. Wang and P. Wu, *Efficient Randomized Communication Without Large Monochromatic Rectangles*, arXiv:2609.20763, 2026. https://arxiv.org/abs/2609.20763
2. D. Gavinsky, *On the quantum communication complexity of total functions*, arXiv:2608.18784, 2026. https://arxiv.org/abs/2608.18784
3. I. Newman, *Private vs. common random bits in communication complexity*, Information Processing Letters 39(2):67--71, 1991. https://doi.org/10.1016/0020-0190(91)90157-D
