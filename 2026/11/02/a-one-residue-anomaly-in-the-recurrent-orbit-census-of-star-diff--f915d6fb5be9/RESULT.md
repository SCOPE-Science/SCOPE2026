# A one-residue anomaly in the recurrent-orbit census of star diffusion

## Finding

Consider synchronous integer diffusion on the labelled star \(K_{1,r}\), with a distinguished center and \(r\ge1\) labelled leaves. Every recurrent orbit is fixed or has primitive period two. Every primitive two-cycle has a unique phase in which the center is strictly below *all* leaves. In that phase it has the form
\[
(c,c+d_1,\ldots,c+d_r),\qquad c\in\mathbb Z,\quad 1\le d_i\le r,
\]
and its partner is
\[
(c+r,c+d_1-1,\ldots,c+d_r-1).
\]
The center-first ordering is used throughout. For each fixed integer total \(S\), set
\[
\alpha_r=\frac{r^r-(-1)^r}{r+1}.
\]
The number of *distinct temporal orbits* of primitive period two at total \(S\) is exactly
\[
C_r(S)=\alpha_r+(-1)^r\mathbf1_{(r+1)\mid S}.
\]
There is precisely one fixed configuration if \((r+1)\mid S\), and none otherwise. Thus the full recurrent configuration count at total \(S\) is \(2C_r(S)+\mathbf1_{(r+1)\mid S}\). The cycle count is almost uniform over the \(r+1\) total-mass residues: the zero residue differs from every other residue by exactly \((-1)^r\) orbit.

If the physical requirement is that *both* phases have nonnegative chips on every vertex, the number \(C_r^+(S)\) of such primitive two-cycle orbits at each nonnegative integer total has generating function
\[
\sum_{S\ge0}C_r^+(S)z^S
=\frac{(z+z^2+\cdots+z^r)^r}{1-z^{r+1}}.
\]
Consequently \(C_r^+(S)=0\) for \(S<r\), \(C_r^+(r)=1\), and \(C_r^+(S)=C_r(S)\) for all \(S\ge r^2\). A fixed state is componentwise nonnegative exactly when its common entry is a nonnegative integer.

## Assumptions and scope

The state space is \(\mathbb Z^{r+1}\); negative integers are allowed for the unrestricted census. The graph is the simple star with one center and \(r\) distinctly labelled leaves. At each round and simultaneously on every edge, one chip moves from the higher endpoint to the lower endpoint, with no transfer for equal endpoint values. Its deterministic map is \(F\). The sum of vertex values \(S\) is invariant. A recurrent configuration here means a periodic point of \(F\); a primitive two-cycle consists of two distinct states interchanged by \(F\). The nonnegative census counts only periodic *orbits entirely contained* in the componentwise nonnegative region; it makes no claim that a general nonnegative initial condition remains nonnegative before reaching periodicity.

## Proof

Write a state as \((c,a_1,\ldots,a_r)\), let \(d_i=a_i-c\), and define \(\epsilon_i=\operatorname{sgn}(d_i)\) and \(H=\sum_i\epsilon_i\). Direct simultaneous application of the rule gives
\[
F(c,a_1,\ldots,a_r)=(c+H,a_1-\epsilon_1,\ldots,a_r-\epsilon_r),
\qquad d_i'=d_i-\epsilon_i-H.
\]

**No recurrent periods greater than two.** For completeness, the standard two-time diffusion potential gives a short self-contained justification. On any finite simple graph, orient each edge once and let \(s_e(t)\) be the sign of the difference of the two oriented endpoint values at time \(t\). Define \(\Phi(t)=\sum_v x_v(t)x_v(t+1)\). Separating the contributions edge by edge yields
\[
\Phi(t+1)-\Phi(t)
=-\sum_{e=uv}\bigl(s_e(t)+s_e(t+1)\bigr)
       \bigl(x_u(t+1)-x_v(t+1)\bigr),
\]
where the orientation used in the sign and difference agrees. Every summand is nonpositive. It is strictly negative if the later sign is nonzero and not the negative of the earlier sign. On a periodic trajectory \(\Phi(t)\) itself is periodic, hence must be constant. No edge can acquire a nonzero sign after a zero sign, and an edge cannot lose its sign permanently and then restore it on a periodic trajectory. Thus each edge sign is either zero throughout or reverses at each step. Its two successive transfers cancel, proving \(F^2(x)=x\) for every periodic state. (This potential and the more general eventual-period theorem are established in the literature; they are not novel ingredients.)

**Classifying the two-cycles.** If \(F^2(x)=x\), then each leaf's transfer over the two rounds is zero, requiring \(\epsilon_i'=-\epsilon_i\). Suppose some \(d_i=0\). Its later sign must also vanish, so the formula above forces \(H=0\). But any positive gap would then change to \(d_i-1\ge0\), preventing sign reversal, and any negative gap to \(d_i+1\le0\), also preventing reversal. Hence all gaps must be zero, giving a fixed state. Likewise, if positive and negative gaps coexist, a positive gap can reverse only when \(H\ge d_i\ge1\), whereas a negative gap can reverse only when \(H\le d_j\le-1\), a contradiction. All nonfixed periodic states therefore have gaps of one strict sign.

If all gaps are positive, then \(H=r\) and \(d_i'=d_i-(r+1)\). All signs reverse precisely when \(1\le d_i\le r\). Under this condition, the next state has all gaps strictly negative, its signs are all \(-1\), and the following round returns to the original state. The all-negative case is its unique partner. For any uniform state every edge is tied, so it is fixed; conversely a fixed state must have every leaf tied to the center, since its leaf update is \(-\epsilon_i\). This completes the state classification including \(r=1\).

**Counting at conserved total.** A unique center-lower representative has total
\[
S=(r+1)c+d_1+\cdots+d_r.
\]
Consequently \(C_r(S)\) equals the number of ordered \(r\)-tuples \((d_1,\ldots,d_r)\in\{1,\ldots,r\}^r\) whose sum is \(S\) modulo \(r+1\). Set \(U(z)=z+z^2+\cdots+z^r\) and \(H(z)=1+z+\cdots+z^r\). In \(\mathbb Z[z]/(z^{r+1}-1)\), we have \(H(z)^2=(r+1)H(z)\), and \(U(z)=H(z)-1\). Expanding the power gives the exact congruence
\[
U(z)^r\equiv (-1)^r+\frac{r^r-(-1)^r}{r+1}H(z)
\pmod{z^{r+1}-1}.
\]
Reading the coefficient of the residue class \(S\) proves the claimed one-residue anomaly. The quotient is integral because \(r\equiv-1\pmod{r+1}\).

**Fully nonnegative cycles.** Both phases are componentwise nonnegative exactly when their unique center-lower representative has \(c\ge0\). Indeed, the lowest coordinate in the representative is \(c\), and the partner's coordinates are \(c+r\) and \(c+d_i-1\ge c\). Summing \(z^{(r+1)c+\sum_i d_i}\) over all \(c\ge0\) and \(1\le d_i\le r\) gives the rational generating function. Its lowest nonzero exponent is \(r\), with coefficient one. For \(S\ge r^2\), every tuple of admissible gaps with the required total residue has \(\sum_i d_i\le r^2\le S\), so its required center \(c\) is nonnegative; this proves saturation.

## Verification

A standalone Python 3 script, `verify.py`, implements the update independently of the formula and checks \(F^2(x)=x\) versus the stated fixed/two-cycle characterization for 789,355 integer gap configurations across \(1\le r\le5\). It separately enumerates the residue counts for \(1\le r\le7\) (35 residue classes), and compares the nonnegative orbit enumerator against independent polynomial convolution for 340 graph-size/total combinations through \(r=6\). The recorded output is in `verify_output.txt` and ends with `STAR_DIFFUSION_CENSUS_VERIFIED`. Finite tests support the proof; they are not substituted for the all-size argument.

## Relationship to prior work

Duffy, Lidbetter, Messinger and Nowakowski introduced the integer diffusion game and established eventual tightness with an explicit preperiod bound on stars (their Section 3.2, Lemma 3.5 and Theorem 3.6). That result implies every orbit eventually has period one or two, but it does not enumerate the periodic orbits at a conserved total. Long and Narayanan later proved eventual period at most two for arbitrary graphs using the two-time potential; that general period theorem likewise does not count star recurrent states. The present conclusion adds the unique-gap parameterization, the residue-wise exact orbit count, and the fully nonnegative orbit generating function. The general two-time potential argument is acknowledged as existing mathematics.

## Limitations

This is a classification of periodic configurations and fully nonnegative periodic orbits, not a census of all attraction basins or transient lengths. For unrestricted integer states there are infinitely many possible starting configurations per conserved total; only the recurrent subset is finite. The nonnegative generating series does not count initial configurations that may temporarily become negative. No claim of priority is made beyond the accessible published sources and research records checked; unindexed historical equivalence remains possible. No independent audit has been performed.

## References

1. C. Duffy, T. F. Lidbetter, M. E. Messinger, R. J. Nowakowski, *A Variation on Chip-Firing: the diffusion game*, arXiv:1609.05792, first posted 19 September 2016, Section 3.2. https://arxiv.org/abs/1609.05792
2. J. Long and B. Narayanan, *Diffusion on graphs is eventually periodic*, arXiv:1704.04295, first posted 13 April 2017, Theorem 1.1 and its potential argument. https://arxiv.org/abs/1704.04295
