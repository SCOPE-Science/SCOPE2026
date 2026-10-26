# Exact sparse-time observability on Mersenne-multiple Rule 60 rings

## Finding
Consider the one-sided binary additive cellular automaton (elementary Rule 60) on a cyclic ring with \(n=2^a(2^r-1)\) sites. Observe the state of **one fixed cell** at equally spaced times, potentially skipping updates. The exact number of independently recoverable initial-state bits is determined by only two arithmetic quantities: the odd-part gcd of the sampling interval with the Mersenne factor, and its power of two.

**Theorem.** Fix integers \(r\ge2\), \(a\ge0\), and \(q\ge1\), and set
\[
n=2^a(2^r-1),\quad m=2^r-1,\quad q=2^bu,\quad u\text{ odd},\quad g=\gcd(u,m).
\]
Define
\[
h=\begin{cases}m-1,&g=1,\\m/g,&g>1,\end{cases}
\qquad e_0=\left\lceil\frac{2^a}{q}\right\rceil,
\qquad e_1=2^{\max(a-b,0)}.
\]
For every binary initial configuration, the time-decimated observation map
\[
\mathcal O_{n,q}(x)=(x_0(0),x_0(q),x_0(2q),\ldots)
\]
has linear rank
\[
\boxed{R(n,q)=e_0+e_1h.}
\]
The first \(R(n,q)\) scalar observations are linearly independent as functionals of the initial state. All observations after them are linear combinations of these; hence the dimension of the unobservable subspace is \(n-R(n,q)\), and each attainable observation record has exactly \(2^{n-R(n,q)}\) distinct compatible initial states.

Complete initial-state reconstruction is possible if and only if
\[
\boxed{\bigl(a=0\ \text{and}\ \gcd(q,2^r-1)=1\bigr)
\quad\text{or}\quad \bigl(a\ge1\ \text{and}\ q=1\bigr).}
\]
Every fixed observation site has the same rank, by translation symmetry.

## Assumptions and scope
The sites are indexed by \(\mathbb Z/n\mathbb Z\); all state arithmetic is in \(\mathbb F_2\), and the synchronous evolution is
\[
x_j(t+1)=x_j(t)+x_{j-1}(t).
\]
The observer knows the update rule and ring length, observes one stationary site without noise, and retains samples at nonnegative times divisible by the positive integer \(q\). The theorem applies to every such \(r,a,q\), including sampling strides longer than the ring. It makes no claim for other ring-length families, noisy measurements, or observers that move from site to site.

## Proof
**1. Observation rows are cyclic powers.** Write \(S\) for the cyclic shift and \(F=I+S\). In the group algebra \(A=\mathbb F_2[X]/(X^n-1)\), the coefficient vector of a fixed-site functional after \(jq\) updates corresponds, up to reversing cyclic indices, to the polynomial \((1+X)^{jq}\). Therefore the rank of the sampled rows is the linear dimension of the span of
\[
1,H,H^2,\ldots\quad\text{inside } A,
\qquad H=(1+X)^q.
\]
If \(\mu_H\) denotes the monic polynomial of least degree annihilating \(H\) in \(A\), then \(1,H,\ldots,H^{\deg\mu_H-1}\) are linearly independent, while \(\mu_H(H)=0\) makes every higher power dependent. Consequently \(R(n,q)=\deg\mu_H\).

**2. Local decomposition.** Since \(m=2^r-1\) is odd and \(n=2^am\), characteristic two gives
\[
X^n-1=(X^m-1)^{2^a}.
\]
Over \(K=\mathbb F_{2^r}\), the polynomial \(X^m-1\) has exactly \(m\) distinct roots, namely all elements of \(K^\times\). After extending scalars to \(K\), the algebra becomes the direct product of local rings \(K[w]/(w^{2^a})\), one for each root \(\zeta\), with \(X=\zeta+w\). Scalar extension preserves the degree of the minimal polynomial.

**3. The zero eigenvalue.** At \(\zeta=1\), the sampled operator is \(H=w^q\). Its minimal polynomial on this local ring is \(Y^{e_0}\), where \(e_0=\lceil 2^a/q\rceil\).

**4. Nonzero eigenvalues and their multiplicities.** At each \(\zeta\ne1\), put \(c=1+\zeta\ne0\), and factor \(q=2^bu\) with odd \(u\). In characteristic two,
\[
H=(c+w)^q=c^q+c^{q-2^b}w^{2^b}+\text{terms divisible by }w^{2^{b+1}}.
\]
The displayed leading coefficient is nonzero because \(u\) is odd. Thus \(H-c^q\) has \(w\)-adic order exactly \(2^b\), so the local factor of its minimal polynomial is \((Y-c^q)^{e_1}\), with \(e_1=\lceil 2^a/2^b\rceil=2^{\max(a-b,0)}\). When several roots \(\zeta\) give the same \(c^q\), these local factors contribute their **maximum** exponent, not their sum, to the least common multiple.

**5. Exact spectral collision count.** The map \(\zeta\mapsto c=1+\zeta\) bijects \(K^\times\setminus\{1\}\) with \(K^\times\setminus\{1\}\). Because the squaring automorphism is bijective on this multiplicative group, the number of distinct values \(c^q\) is the number of images under \(c\mapsto c^u\). The latter homomorphism has kernel of size \(g=\gcd(u,m)\) and image size \(m/g\). Removing the input \(c=1\) deletes its output if and only if \(g=1\). Thus the number of distinct nonzero eigenvalues is exactly \(h\). The zero factor is coprime to all nonzero factors, giving
\[
\deg\mu_H=e_0+e_1h.
\]
This establishes the rank, first-observation independence, and the exact nullity.

**6. Reconstruction criterion.** If \(a=0\), then \(e_0=e_1=1\) and \(R=n\) exactly when \(g=1\), equivalently \(\gcd(q,m)=1\). If \(a\ge1\), the stride \(q=1\) gives \(e_0=e_1=2^a\), \(h=m-1\), hence \(R=n\). For every \(q>1\), if \(b>0\), then \(e_1<2^a\) and \(e_0\le2^a\), forcing \(R<n\). If \(b=0\) and \(q>1\), then \(e_0<2^a\) while \(h\le m-1\), also forcing \(R<n\). Therefore no genuine temporal thinning reconstructs an even-length ring in this family.

## Verification
The accompanying standalone `verify.py` computes actual sampled observation row vectors through cyclic Boolean convolution and measures their binary rank by independent pivot elimination, without using the spectral derivation. It checks 528 parameter triples exhaustively over the programmed grid, plus 216 reproducibly chosen larger-parameter triples. All 744 tested ranks agree with the theorem. Illustrative exact ranks are
\[
R(7,1)=7,\quad R(7,7)=2,\quad R(14,3)=13,\quad R(14,7)=3,\quad R(30,3)=11,\quad R(30,7)=29.
\]
Run `python verify.py` using Python 3 and no external libraries. Computations corroborate, but do not replace, the proof for unbounded parameters.

## Relationship to prior work
Classical work of Wolfram (1983) and Martin–Odlyzko–Wolfram (1984) develops elementary and additive cellular-automaton dynamics. El Yacoubi and collaborators (2021) establish general observability and reconstructibility frameworks, including rank-based tests for affine cellular automata. Their general rank criterion can assess any fixed numerical instance; the present theorem evaluates the entire infinite arithmetic family in closed form and proves the sharp initial-segment and perfect-reconstruction assertions for *one-site, fixed-stride sampling*. Elser's 2021 reconstruction paper instead infers an unknown automaton rule from nonconsecutive full-state snapshots.

Other relevant work includes Plénet and collaborators' papers on bounded and affine cellular-automaton observability in 2022. Their available abstracts emphasize general criteria, mobile sensors, and random-number reconstruction. Complete texts were not accessible for decisive line-by-line comparison, so historical priority relative to these works remains a scientific limitation, not a claim that they were ruled out.

## Limitations
The theorem assumes perfect, deterministic Boolean dynamics on the stated Mersenne-multiple ring lengths, a single stationary observation site, and regularly sampled times. It does not imply robustness to noise, a condition number, sparse-site optimality for multiple observers, or an analogous closed form for arbitrary lengths. The sampled rank and uniqueness result are proved; broader novelty against all historical sources is not independently certified. The 2022 observability articles could be inspected only at abstract level, leaving a specific historical-priority risk.

## References
1. S. Wolfram, “Statistical Mechanics of Cellular Automata,” *Reviews of Modern Physics* **55**, 601–644 (1983). https://doi.org/10.1103/RevModPhys.55.601
2. O. Martin, A. M. Odlyzko, and S. Wolfram, “Algebraic Properties of Cellular Automata,” *Communications in Mathematical Physics* **93**, 219–258 (1984). https://www-users.cse.umn.edu/~odlyzko/doc/arch/cellular.automata.pdf
3. S. El Yacoubi, T. Plénet, S. Dridi, F. Bagnoli, L. Lefèvre, and C. Raïevsky, “Some Control and Observation Issues in Cellular Automata,” *Complex Systems* **30**, 391–413 (2021). https://doi.org/10.25088/ComplexSystems.30.3.391
4. V. Elser, “Reconstructing Cellular Automata Rules from Observations at Nonconsecutive Times,” *Physical Review E* **104**, 034301 (2021), preprint arXiv:2012.02179. https://arxiv.org/abs/2012.02179
5. T. Plénet et al., “Observability and Reconstructibility of Bounded Cellular Automata,” *International Journal of Systems Science* **53**, 2901–2917 (2022). https://doi.org/10.1080/00207721.2022.2064556
6. T. Plénet et al., “Observability and Reconstructibility of Affine Cellular Automata: Example on Random Number Reconstruction,” *Journal of Cellular Automata* **16**, 401–422 (2022). https://www.oldcitypublishing.com/journals/jca-home/jca-issue-contents/jca-volume-16-number-5-6-2022/jca-16-5-6-p-401-422/
