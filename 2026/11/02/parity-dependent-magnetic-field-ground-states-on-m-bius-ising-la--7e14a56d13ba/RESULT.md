# Parity-dependent magnetic-field ground states on Möbius Ising ladders

## Finding

A uniform classical antiferromagnet on the cubic Möbius ladder has a finite-field transition at \(|h|=J\) **if and only if** its half-circumference \(n\) is even. At that transition the number of distinct labelled ground-state spin configurations is exactly \(4n\). For \(J<|h|<3J\), the total magnetization is just \(2\operatorname{sgn}(h)\), independently of the system size, whereas below \(J\) it is zero. Odd half-circumferences show no such intermediate regime.

The result is a complete finite-size, zero-temperature field classification for every \(n\ge3\), not a claim of a new bulk thermodynamic phase. The saturation-field independent-set count and the even-\(n\) zero-field degeneracy are previously known ingredients, explicitly credited below.

## Assumptions and scope

Let \(M_{2n}\), \(n\ge3\), have vertices \(\mathbb Z/(2n\mathbb Z)\), cycle edges \(\{i,i+1\}\), and antipodal edges \(\{i,i+n\}\). All edges are distinct and the graph is connected and cubic with \(3n\) edges. For \(\sigma_i\in\{-1,+1\}\), \(J>0\) and \(h\in\mathbb R\), define

\[
H(\sigma)=J\sum_{\{i,j\}\in E(M_{2n})}\sigma_i\sigma_j-h\sum_{i=0}^{2n-1}\sigma_i.
\]

Write \(b=|h|\). The exact ground energy for odd \(n\) is

\[
E_0=\begin{cases}-3nJ,&0\le b\le3J,\\ 3nJ-2nb,&b\ge3J.\end{cases}
\]

For even \(n\), it is

\[
E_0=\begin{cases}-3nJ+4J,&0\le b\le J,\\-3nJ+6J-2b,&J\le b\le3J,\\3nJ-2nb,&b\ge3J.\end{cases}
\]

The two formulas agree at all indicated shared endpoints. Let

\[
I_n=(1+\sqrt 2)^n+(1-\sqrt 2)^n-(-1)^n.
\]

The **total number of labelled spin configurations** attaining the minimum (not divided by translations or spin reversal) is

| Range | Odd \(n\) | Even \(n\) |
|---|---:|---:|
| \(b=0\) | \(2\) | \(2n\) |
| \(0<b<J\) | \(2\) | \(2n\) |
| \(b=J\) | \(2\) | \(4n\) |
| \(J<b<3J\) | \(2\) | \(2n\) |
| \(b=3J\) | \(I_n\) | \(I_n\) |
| \(b>3J\) | \(1\) | \(1\) |

The magnetization away from transition fields, expressed as \(\sum_i\sigma_i\), is \(0\) below saturation for odd \(n\), and for even \(n\) is \(0\) when \(b<J\), and \(2\operatorname{sgn}(h)\) when \(J<b<3J\). Beyond saturation it is \(2n\operatorname{sgn}(h)\). At transition fields the listed distinct ground configurations can have different magnetizations.

## Proof

**1. Convert spin energy into a cut-and-independence problem.** By spin reversal it suffices to take \(h\ge0\). Let \(S\) be the vertices carrying spin \(-1\), \(t=|S|\), and \(e(S)\) the number of graph edges with both endpoints in \(S\). Since the graph is cubic, the cut has \(3t-2e(S)\) edges. Consequently the exact identity is

\[
H=3nJ-2nh+2(h-3J)t+4Je(S).
\]

For \(h>0\) a minimizer can have \(t\le n\), as otherwise replacing \(S\) by its complement preserves the exchange energy but strictly improves the field energy. At \(h=0\), complementation leaves energy unchanged and can be handled symmetrically.

**2. Determine independence and near-independence at the twisted boundary.** Represent the vertices as \(n\) antipodal rungs with binary occupancies \((a_i,b_i)\). An independent set has at most one occupied vertex in each rung. Adjacent rungs forbid repeated occupancy on the same leg, while the closing link is twisted: its two links interchange the legs. If \(n\) is odd, all \(n\) rungs can be singly occupied and alternating, producing exactly two independent sets of size \(n\). Conversely any size-\(n\) independent set must fill all rungs singly and hence be one of these two.

If \(n\) is even, filling all rungs singly without an internal edge is impossible, because alternation around the twisted boundary has inconsistent parity. An independent set therefore has size at most \(n-1\). That maximum is achieved by leaving exactly one rung empty, and there are exactly \(n\) choices of empty rung times two choices of alternating orientation, i.e. \(2n\) maximum independent sets.

Moreover, in the even case any set with \(t=n\) must contain at least one internal edge, and exactly \(2n\) such sets have \(e(S)=1\). Indeed, if an occupied rung held two particles, its rung would already provide an internal edge, and at least one neighboring occupied rung would provide another (as only one empty rung can compensate in a size-\(n\) set); thus \(e(S)=1\) forces exactly one occupied vertex on every rung. The twisted, odd-parity sequence of single-leg choices must then have an odd number of violations, exactly one in the minimal case. Its position has \(n\) choices and its initial orientation has two.

**3. Minimize for every field.** For odd \(n\), the maximum independent-set size \(n\) gives \(e(S)=0\). Thus for \(0<h<3J\) the coefficient of \(t\) in step 1 is negative, and the unique optimal size is \(t=n\) with precisely two configurations. For \(h>3J\) it is \(t=0\). For even \(n\), among \(t\le n-1\), the unique optimal size for \(0<h<3J\) is \(n-1\) with \(e(S)=0\), while the only competitor at \(t=n\) has \(e(S)\ge1\). The latter improves on the former by precisely \(2(J-h)\) in energy. Hence it wins for \(h<J\), ties for \(h=J\), and loses for \(J<h<3J\). The counts are \(2n,4n,2n\), respectively. For \(h>3J\), \(t=0\) uniquely minimizes. Substituting each winning \((t,e(S))\) into step 1 gives the stated piecewise energies. At \(h=0\), the same even-rung near-independent configurations have \(t=n\), and spin reversal adds no new configurations; odd-rung states remain the two bipartite colorings.

**4. Count the saturation degeneracy.** At \(h=3J\), step 1 reduces to a positive multiple of \(e(S)\), so the exact ground space is the set of **all independent sets**, including the empty set. For a transfer description use rung states \(O=(0,0)\), \(A=(1,0)\), and \(B=(0,1)\). The straight transition matrix and twisted closure are

\[
T=\begin{pmatrix}1&1&1\\1&0&1\\1&1&0\end{pmatrix},\qquad
P=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}.
\]

The independent-set count is \(\operatorname{tr}(PT^n)\). The eigenvalues of \(T\) are \(1+\sqrt2\), \(1-\sqrt2\), and \(-1\); the corresponding eigenvalues of \(P\) are \(1,1,-1\). This proves the displayed formula for \(I_n\). Its closed form is independently documented in the existing Möbius-ladder independence-polynomial literature and is **not** asserted as a new combinatorial formula. Finally, spin reversal extends every case from nonnegative to all real \(h\).

## Verification

The standalone Python-standard-library script `check_mobius.py` independently constructs energies from the cycle and antipodal edge cuts, exhaustively enumerates all \(2^{2n}\) labelled spin configurations for \(3\le n\le10\), and checks both minimum energies and multiplicities at 14 positive, negative, and critical field values. It also independently constructs a four-state twisted-boundary transfer recurrence for \(3\le n\le64\), comparing exact integer minimum energies and degeneracies with the theorem. Run `python3 check_mobius.py` from this directory. The exact stored output is in `CHECK_OUTPUT.txt`.

These tests verify **112 exhaustive field cases** involving **1,398,080 total spin configurations**, plus **868 independently constructed transfer cases** and eight independent-set enumerations. Finite tests corroborate rather than prove the arbitrary-\(n\) statement; the proof above supplies the infinite-family argument.

## Relationship to prior work

Lu and Wu's 2000 Möbius-strip Ising partition-function calculation treats zero applied longitudinal field and general strip widths, and hence does not give the stated finite-field crossing. Kalinin and Berloff (2022) explicitly identify the even-Möbius-ladder **zero-field** two-frustrated-edge states and their \(2n\) count; this known fact is credited rather than relabelled. Varma (2013) explains saturation at coordination-number field in other Ising ladders, including the association with independent-set counting. The Möbius-ladder independence polynomial already gives \(I_n\) at saturation (MathWorld and cited combinatorial references). Cummins and Berloff (2025) analyze Möbius couplings in an Ising optimization model, rather than the exact all-field finite-size degeneracy.

The specific additional statement is the parity-selective **field \(J\)** crossing, its exact \(4n\) multiplicity, the size-independent magnetization-\(2\) interval, and the simultaneous complete enumeration of all ground-state phases. A failed literature search alone is not proof of historical priority; a specialized stronger classification might exist.

## Limitations

This is an exact **classical zero-temperature** theorem for uniform antiferromagnetic exchange on an unweighted cubic Möbius ladder. It neither addresses finite-temperature thermodynamics nor unequal couplings, disorder, quantum spins, open ladders, or annealer dynamics. The intermediate magnetization per spin is \(1/n\) and therefore vanishes at large system size: the \(h=J\) feature is a finite-size twist effect, not a claimed bulk phase transition. The saturation-point entropy per site tends to \(\tfrac12\log(1+\sqrt2)\) in natural units, a consequence of a previously known independent-set count. Independent priority and experimental validation have not been performed.

## References

- W. T. Lu and F. Y. Wu, *Ising model on nonorientable surfaces: Exact solution for the Moebius strip and the Klein bottle* (public preprint, 20 July 2000), https://arxiv.org/abs/cond-mat/0007325.
- V. K. Varma, *Saturation field entropies of antiferromagnetic Ising models: Ladders and the kagome lattice* (public preprint, 20 May 2013), https://arxiv.org/abs/1305.4606.
- K. P. Kalinin and N. G. Berloff, *Computational complexity continuum within Ising formulation of NP problems*, Communications Physics 5 (2022), https://www.nature.com/articles/s42005-021-00792-0.
- J. S. Cummins and N. G. Berloff, *Vector Ising spin annealer for minimizing Ising Hamiltonians*, Communications Physics 8 (2025), https://www.nature.com/articles/s42005-025-02145-7.
- *Möbius Ladder*, Wolfram MathWorld, https://mathworld.wolfram.com/MoebiusLadder.html (independence-polynomial formula; access date not used as public-preprint date).
