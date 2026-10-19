# Closed dihedral orbit series and a parity obstruction in modular gap shifts

## Finding

For each integer \(r\ge 2\), let \(X_r\subseteq\{0,1\}^{\mathbb Z}\) consist of all binary sequences in which every pair of *successive* occurrences of \(1\) is separated by a number of zeros divisible by \(r\). Thus the permitted successive-marker distances are \(1,1+r,1+2r,\ldots\); the all-zero point is included. The shift is \((\sigma x)_i=x_{i+1}\), and the coordinate-reversal flip is \((Fx)_i=x_{-i}\).

Write \(p_n=|\operatorname{Fix}(\sigma^n)|\) and \(p_{n,k}=|\operatorname{Fix}(\sigma^n)\cap\operatorname{Fix}(\sigma^kF)|\), for integers \(n\ge1\) and \(k\). Define the three complete reflection-count series
\[
 O_r(z)=\sum_{m\ge0}p_{2m+1,0}z^m,\qquad
 V_r(z)=\sum_{m\ge1}p_{2m,0}z^m,\qquad
 E_r(z)=\sum_{m\ge1}p_{2m,1}z^m.
\]
Put
\[
 d_r=\frac{r}{\gcd(r,2)},\qquad
 Q_r(z)=1-z-z^r,\qquad
 A_r(z)=\frac1{1-z^{d_r}},\qquad
 C_r(z)=\frac{1-z^r}{Q_r(z)},
\]
and
\[
 B_r(z)=\begin{cases}0,&r\text{ even},\\
 \displaystyle\frac{z^{(r+1)/2}}{1-z^r},&r\text{ odd}.
 \end{cases}
\]
**Theorem.** For every integer \(r\ge2\), as formal power series at zero,
\[
\boxed{\begin{aligned}
 O_r(z)&=\frac1{1-z}+(1+B_r(z))A_r(z)C_r(z),\\
 V_r(z)&=\frac z{1-z}+(1+B_r(z))^2C_r(z)-1,\\
 E_r(z)&=\frac z{1-z}+zA_r(z)^2C_r(z).
\end{aligned}}
\]
The ordinary period counts and Artin–Mazur zeta are
\[
\boxed{p_n=\operatorname{tr}(M_r^n)+1-r\mathbf1_{r\mid n},\qquad
\zeta_{\sigma}(t)=\frac{1-t^r}{(1-t)(1-t-t^r)},}
\]
where \(M_r\) is the \(r\)-state directed-cycle adjacency matrix with one additional loop at state \(0\). The complete infinite-dihedral Lind zeta is consequently
\[
\boxed{\mathcal Z_r(t)=
\left(\frac{1-t^{2r}}{(1-t^2)(1-t^2-t^{2r})}\right)^{1/2}
\exp\left(tO_r(t^2)+\frac{V_r(t^2)+E_r(t^2)}2\right).}
\]
All square roots and exponentials here are the formal series with constant term \(1\).

**Sharp reflection-axis parity dichotomy.** For even \(r\), every nonzero periodic point fixed by a *vertex-axis* reflection has symbol \(1\) at every reflection-fixed vertex; in particular a reflection-fixed vertex carrying \(0\) forces the all-zero orbit. For odd \(r\ge3\), nonzero reflection-symmetric periodic words with a reflection-fixed vertex carrying \(0\) exist, both for odd periods (one fixed vertex) and for even periods (two fixed vertices). Hence the obstruction is exactly parity-sensitive, not an artifact of the series computation.

The formulas include \(r=2\) only as a consistency check: its Lind zeta is already explicitly evaluated by Kim and Ryu (2011, their final example). The uniform closed forms and sharp parity distinction for general \(r\ge3\) are the assessed contribution.

## Assumptions and scope

All shifts are two-sided over the two-symbol alphabet with the product topology. A successive pair of markers means no other marker lies between them. A period count includes points of period dividing \(n\), rather than only least period \(n\). The flip is coordinate reversal, not a symbol-complementing flip. Counts are finite and all generating-function identities are formal around zero; no analytic branch selection beyond constant term \(1\) is needed. The theorem applies for every fixed integer modulus \(r\ge2\), with no upper bound on \(r\) or observation period.

When \(n\) is odd, all reflections \(\sigma^kF\) are conjugate on an \(n\)-cycle. When \(n\) is even, \(k\) even fixes two sites (vertex axes), whereas \(k\) odd fixes no sites (edge axes). These are the only three reflection types encoded by \(O_r,V_r,E_r\).

## Proof

### 1. An exact labeled presentation and its periodic correction

Use states \(0,1,\ldots,r-1\), a zero-labeled transition \(j\to j+1\pmod r\) for each \(j\), and an additional one-labeled loop at state \(0\). Immediately after a marker the state is \(0\); the zero count must return to \(0\) before the next marker. This presents exactly \(X_r\). Its nonnegative adjacency matrix is \(M_r\). The directed-cycle-plus-loop determinant identity is
\[
\det(I-zM_r)=1-z-z^r=Q_r(z).
\]
For a periodic label configuration containing at least one marker, the marker fixes the state phase and there is exactly one periodic edge lift. The all-zero label configuration has \(r\) distinct periodic lifts when \(r\mid n\), and no periodic lift otherwise, because the zero-labeled transitions form a cycle of length \(r\). Since the all-zero configuration is always one point of \(X_r\), the trace correction is exactly \(1-r\mathbf1_{r\mid n}\), proving the formula for \(p_n\). Consequently,
\[
\begin{aligned}
\sum_{n\ge1}\frac{p_n}{n}t^n
&=-\log\det(I-tM_r)-\log(1-t)+\log(1-t^r)\\
&=-\log Q_r(t)-\log(1-t)+\log(1-t^r),
\end{aligned}
\]
which proves the ordinary zeta expression.

### 2. Half-cycle reflection decomposition

For any reflected nonzero periodic word, choose one representative from each pair of non-fixed sites and each fixed site. Its marker positions form a monotone ordered list on a fundamental half-cycle. Any *interior* distance between consecutive markers belongs to \(\{1+rj:j\ge0\}\), and therefore has length generating function
\[
L_r(z)=\frac{z}{1-z^r}.
\]
An arbitrary (possibly empty) succession of such interior gaps has series
\[
\frac1{1-L_r(z)}=\frac{1-z^r}{1-z-z^r}=C_r(z).
\]
There are precisely three relevant ways for a half-cycle to terminate at a reflection axis:

At a **vertex axis**, a marker sitting at the fixed vertex contributes zero half-distance and weight \(1\). If the fixed vertex is unoccupied, the nearest two mirrored markers lie \(h\ge1\) steps away on either side of it; their full separation is \(2h\). Admissibility requires \(2h\equiv1\pmod r\). For even \(r\), this is impossible. For odd \(r\), it means \(h=(r+1)/2+jr\), for \(j\ge0\). Hence the vertex-end factor is exactly \(1+B_r(z)\).

At an **edge axis**, the nearest two mirrored markers lie across a gap of odd length \(2h+1\), where \(h\ge0\). Admissibility is \(2h\equiv0\pmod r\), equivalent to \(h\equiv0\pmod{d_r}\). The edge-end factor is exactly \(A_r(z)\).

For odd period \(2m+1\), the reflection has a vertex axis at one end and an edge axis at the other. Multiplying \((1+B_r)\), \(C_r\), and \(A_r\) counts every nonzero compatible periodic word once, with exponent \(m\). The all-zero point contributes \(1\) at every odd period, giving \(1/(1-z)\) and the formula for \(O_r\).

For even period \(2m\) with a vertex–vertex reflection, both ends have factor \(1+B_r\) and their internal gaps contribute \(C_r\). Their constant term \(1\) corresponds to the nonexistent period-zero case and must be discarded. Adding the all-zero point at each positive even period gives \(z/(1-z)\), proving the formula for \(V_r\).

For even period \(2m\) with an edge–edge reflection, the two ends contribute \(A_r^2\). Because there are no fixed vertices, there is at least one marker in the chosen half. That marker accounts for the extra factor \(z\), after which the gaps contribute \(C_r\). Adding the all-zero point yields the formula for \(E_r\). This proves all three identities by bijective half-cycle decomposition, not by inference from a finite enumeration.

### 3. The exact parity obstruction and sharpness

Suppose \(r\) is even and a nonzero reflected periodic sequence has an unoccupied fixed vertex. Its nearest markers to the left and right of that vertex must be mirror images. Their distance is even, whereas every allowed marker-to-marker distance is \(1\pmod r\), hence odd. This contradiction proves the obstruction. With two reflection-fixed vertices, the same argument applies at each vertex separately.

For odd \(r\ge3\), let \(h=(r+1)/2\). In the odd-period \(n=r+2\) word with markers at residues \(h\) and \(h+1\) and zeros elsewhere, successive marker distances are \(1\) and \(r+1\), both allowed. Reflection \(i\mapsto-i\pmod n\) interchanges the two markers, and its unique fixed vertex \(0\) is unoccupied. In the even-period \(n=2(r+1)\) word with markers at \(h\) and \(n-h\), both marker distances are \(r+1\), and reflection about vertices \(0\) and \(r+1\) fixes the word while both vertices carry \(0\). Thus the odd-modulus failure is realized in both parity classes.

### 4. Lind zeta normalization

The standard infinite-dihedral zeta of \((X_r,\sigma,F)\) is
\[
\mathcal Z_r(t)=\zeta_\sigma(t^2)^{1/2}
\exp\left(\sum_{m\ge1}
 \left[p_{2m-1,0}t^{2m-1}
 +\frac{p_{2m,0}+p_{2m,1}}{2}t^{2m}\right]\right).
\]
Substitution of the three series gives precisely the boxed expression above. This normalization agrees algebraically with the already published \(r=2\) even-shift expression; that base case is not a new result.

## Verification

The included `verify.py` independently enumerates cyclic binary words whose gaps satisfy the modular rule; it does *not* use the half-cycle bijection to generate its test configurations. For each \(2\le r\le8\), it counts reflection-invariant cyclic words directly from orbits of \(i\mapsto k-i\pmod n\), compares their exact integer counts with coefficients of the three claimed rational series, and independently counts cyclic words against the trace formula for \(M_r\). In total, there are 322 exact comparisons. The verifier also has no floating-point input and no external dependencies.

An independent symbolic calculation verified that the \(r=2\) Lind zeta exponent reduces identically to the published numerator \(2t+2t^2-t^3-t^4-2t^5-t^6\) divided by \((1-t^2)(1-t^2-t^4)\). These finite and symbolic tests check formula normalization but do not replace the unrestricted proofs in Sections 1–4.

## Relationship to prior work

Kim and Ryu, *On the number of fixed points of sofic flip systems* (arXiv:1112.4706v1, 2011-12-20), prove a general finite-matrix computation theorem for reversal-fixed counts on any sofic flip system (Theorem B), and explicitly compute the full Lind zeta for the \(r=2\) even shift in their final example. In particular, the existence and rationality of the generating function and the concrete \(r=2\) evaluation are not original here. Applying their general theorem separately at any fixed \(r\) also supplies a route to these counts, but does not give the displayed uniform formulas, their half-axis residue decomposition, or the sharp parity obstruction as an explicit across-modulus classification.

Ryu, *On conjugacy invariants of \(D_\infty\)-topological Markov chains* (arXiv:1407.3988), develops the broader dynamical context of flip pairs, Lind zeta and conjugacy invariants. Its worked examples concern particular finite-state systems and do not state the present closed formulas for modular binary gap shifts. A separate accessible published mathematical record on embeddings of modular gap shifts analyzes a divisibility obstruction for shift-commuting embeddings; that embedding classification is a different invariant and does not enumerate reflection-fixed periodic words.

The paper-level overlap comparison is deliberately stronger than title comparison: Theorem B is a genuine general covering *algorithm* and the known \(r=2\) formula is a covered special case. The assessed additional fact is the explicit full-family evaluation, with an exact even/odd obstruction and witnesses. Independent historical-priority verification remains outstanding.

## Limitations

The theorem is restricted to the coordinate-reversing flip on binary modular-gap shifts, not general symbol-permuting flips, arbitrary renewal gap sets, or infinite alphabets. The results are exact for every finite modulus and period, but do not provide sharp uniform asymptotics as \(r\) and period grow jointly. Because a general published sofic flip formula can be specialized algorithmically, the priority of the closed family evaluation requires external expert comparison; no claim of complete historical uniqueness or independent certification is made.

## References

1. Y.-O. Kim and S. Ryu, *On the number of fixed points of sofic flip systems*, arXiv:1112.4706v1 (first posted 2011-12-20), https://arxiv.org/abs/1112.4706 . Theorem B and the final even-shift example.
2. S. Ryu, *On conjugacy invariants of \(D_\infty\)-topological Markov chains*, arXiv:1407.3988 (first version 2014), https://arxiv.org/abs/1407.3988 . See the flip-pair invariants and examples.
3. Y.-O. Kim, J. Lee and K. K. Park, *A zeta function for flip systems*, Pacific Journal of Mathematics 209 (2003), 289–301, DOI:10.2140/pjm.2003.209.289 . Standard infinite-dihedral zeta normalization.
