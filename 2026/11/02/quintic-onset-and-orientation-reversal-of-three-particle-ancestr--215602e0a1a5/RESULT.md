# Quintic onset and orientation reversal of three-particle ancestral circulation

## Finding

Let three Fleming–Viot particles move independently on the complete graph with sites \(\{0,1,2\}\), jumping at rate one along each directed edge. A particle at site \(i\) is killed at rate \(k_i\), then instantaneously copies the site and ancestral label of one of the other two particles, chosen uniformly. Copying at coincident sites is included. The unique stationary count law is \(\pi_3\). If \(h_3(j,d)\) is the eventual fixation probability of one specified ancestral label currently at \(j\), given that the other two particles have count vector \(d\), define

\[
F_{ij}^{(3)}=\sum_{c:c_i>0}\pi_3(c)c_i h_3(j,c-e_i),\qquad
\Delta_3(k)=F_{02}^{(3)}-F_{20}^{(3)}.
\]

**Theorem.** For \(k=(1-\varepsilon,1,1+\varepsilon)\) and \(|\varepsilon|<1\),

\[
\boxed{\Delta_3(1-\varepsilon,1,1+\varepsilon)
=\frac{89}{56010528}\varepsilon^5+O(\varepsilon^7)
\quad(\varepsilon\to0).}
\]

In particular, the current is strictly positive for all sufficiently small positive \(\varepsilon\). On the same graph, the published cubic coefficient for each fixed population \(N\ge4\) is strictly negative [1, Section 5 and Appendix B]. Hence the direction of the leading ancestral circulation reverses between three and four particles along exactly this killing-rate perturbation. The new result is the **three-particle quintic law**; the larger-population cubic law is cited, not claimed anew.

## Assumptions and scope

The particle population is exactly three; the motion rates are \(q(i,j)=1\) for \(i\ne j\); killing rates are positive, with \(|\varepsilon|<1\); and each killed particle chooses uniformly between the two survivors. The current weights **eventual survival of the ancestral label**, not merely current particle counts or immediate copying events. Every initial count configuration is allowed. The assertion is a local asymptotic as \(\varepsilon\to0\), not a claim of the current's sign on the entire interval \((0,1)\).

Let \(\Omega=\{c\in\mathbb N_0^3:\sum_i c_i=3\}\) (ten states) and \(\mathcal H=\{(i,d):i\in\{0,1,2\},\ d\in\mathbb N_0^3,\ \sum_a d_a=2\}\) (eighteen states). In formulas, \(e_i\) is the \(i\)-th coordinate vector. All finite matrices below are uniquely determined by these sets, in the lexicographic ordering supplied by `verify.py`.

## Proof

**1. Finite stationary and founder equations.** For distinct sites \(a,b\), the off-diagonal population generator is

\[
L_k(c,c-e_a+e_b)=c_a+\frac{c_ac_bk_a}{2},
\]

with diagonal entries chosen to make each row sum zero. This counts natural jumps and deaths followed by copying a particle at a different site. The stationary row vector satisfies \(\pi_k L_k=0\) and \(\sum_c\pi_k(c)=1\).

The founder operator on a function \(h:\mathcal H\to\mathbb R\) is

\[
\begin{aligned}
(T_kh)(i,d)={}&\sum_{j\ne i}\bigl[h(j,d)-h(i,d)\bigr]-k_i h(i,d)\\
&+\sum_a d_a\sum_{b\ne a}\bigl[h(i,d-e_a+e_b)-h(i,d)\bigr]\\
&+\sum_a d_ak_a\left[h(i,d-e_a+e_i)
+\frac12\sum_b(d_b-\mathbf1_{\{a=b\}})h(i,d-e_a+e_b)-h(i,d)\right].
\end{aligned}
\]

Terms with zero combinatorial coefficients are omitted. This follows by distinguishing a founder, letting each other particle move, die and choose a donor, and adding the two descendant contributions when the founder is copied. Its unique normalized null vector is the founder fixation law, with \(T_kh_k=0\) and \(h_k(0,2e_0)=1/3\). The equations agree with [1, Appendix A, equations (A.1) and (A.4)]. Finiteness, irreducibility of the count chain and almost-sure eventual founder fixation justify both normalizations.

**2. Exact perturbation recursion.** Write \(s=(-1,0,1)\), \(k(\varepsilon)=\mathbf1+\varepsilon s\), \(L_{k(\varepsilon)}=L_0+\varepsilon L_1\), and \(T_{k(\varepsilon)}=T_0+\varepsilon T_1\). Since the constrained stationary and founder matrices are nonsingular at zero, both solutions are analytic near zero. Write

\[
\pi(\varepsilon)=\sum_{r\ge0}\pi_r\varepsilon^r,
\qquad h(\varepsilon)=\sum_{r\ge0}h_r\varepsilon^r.
\]

Here \(h_0\equiv1/3\); for \(r\ge1\), exact coefficient comparison gives

\[
\begin{aligned}
\pi_rL_0&=-\pi_{r-1}L_1,&\sum_c\pi_r(c)&=0,\\
T_0h_r&=-T_1h_{r-1},&h_r(0,2e_0)&=0.
\end{aligned}
\]

The normalized order-zero stationary vector is the unique \(\pi_0\) satisfying \(\pi_0L_0=0\) and \(\sum_c\pi_0(c)=1\). Define

\[
G_r(c)=c_0h_r(2,c-e_0)-c_2h_r(0,c-e_2),
\]

where a term with its respective count zero is interpreted as zero. The coefficient of \(\varepsilon^r\) in \(\Delta_3\) is exactly

\[
d_r=\sum_{a=0}^r\sum_{c\in\Omega}\pi_a(c)G_{r-a}(c).
\]

**3. Exact rational evaluation.** Solving the fixed \(10\times10\) and \(18\times18\) rational systems by Gaussian elimination through degree five gives the following ordered contributions \(\sum_c\pi_a(c)G_{r-a}(c)\), in increasing \(a\):

- Degree one: \(-4/21,\ 4/21\), with sum zero.
- Degree three: \(11/10584,\ 325/42336,\ -283/32928,\ -1/8232\), with sum zero.
- Degree five: \(-121/6001128,\ -3539/96018048,\ 1349/12446784,\ -83/4741632,\ 173/3687936,\ -73/921984\), with sum \(89/56010528\).

Every displayed fraction is an **exact rational** output of the explicit coefficient recursions, not a floating-point estimate. `verify.py` constructs the complete matrices from their transition definitions, performs all eliminations in Python's `fractions.Fraction`, checks each coefficient and normalization, and reproduces the independently published nonperturbative benchmark

\[
\Delta_3(1,2,4)=\frac{421413160}{139117744582101}
\]

from [1, Appendix A]. These identities furnish a finite algebraic certificate for the only nontrivial arithmetic step.

**4. Oddness and positivity.** Interchanging sites \(0\) and \(2\) sends \(\varepsilon\) to \(-\varepsilon\) and reverses the signed edge current. Consequently \(\Delta_3(-\varepsilon)=-\Delta_3(\varepsilon)\). All even coefficients vanish, the first and third coefficients above vanish, and the positive fifth coefficient yields the claimed \(O(\varepsilon^7)\) remainder and strict local positivity. The negative cubic coefficient for \(N\ge4\) in [1] proves the stated orientation comparison. \(\square\)

## Verification

Run `python3 verify.py` with Python 3. The script uses only the standard library and verifies the exact Taylor coefficient list \(0,0,0,0,0,89/56010528\), the normalization identities, and the published benchmark \(421413160/139117744582101\). Its recorded output appears in `CHECKER_OUTPUT.txt`. A separate symbolic-rational implementation was also used to check coefficients through degree nine, yielding the same fifth coefficient. No finite random simulation is used as evidence for the local asymptotic: analyticity plus exact finite-dimensional coefficient algebra proves the statement for a continuum of nearby parameters.

## Relationship to prior work

Lin and Lu [1] define the ancestral current, prove its generic nonvanishing for three or more particles, give a numerical-rational exact example at killing vector \((1,2,4)\), and derive an explicit cubic perturbation coefficient for \(N\ge4\). They expressly identify the cubic cancellation when \(N=3\) (Section 5) but do not supply the leading nonzero term in that exceptional population. The present quintic coefficient and its **opposite orientation** fill that precise natural gap.

The authors' related Brownian paper [2] concerns a different continuous-space transport model and obtains a cubic current from a two-harmonic spatial killing profile; it does not determine the discrete triangle's exceptional fifth-order coefficient. Cloez and Thai [3] derive stationary results on a complete graph under **uniform** killing, and Corujo [4] studies cycle graphs with uniform killing, so neither heterogeneous-killing model supplies the claim. These comparisons concern mathematical implications, not mere titles.

## Limitations

The result is local near homogeneous killing and is specific to exactly three particles on the three-site complete graph, with uniform donor choice and the paper's survival-weighted current. It does not classify current sign for all positive killing vectors, all motion graphs, larger populations, or other definitions of transport. The larger-population contrast follows from [1], not a new proof. Originality remains qualified pending independent historical-priority review, including the possibility of a more general resolvent identity not found in the inspected literature. Scientific verification here is self-review only.

## References

[1] Y. Lin and T. Lu, *Ancestral circulation beyond two Fleming–Viot particles*, arXiv:2610.12589v1, first public 2026-10-08. https://arxiv.org/abs/2610.12589 . Especially Sections 3–5 and Appendices A–B.

[2] Y. Lin and T. Lu, *Branching explosion of Brownian Fleming–Viot systems*, arXiv:2610.18802v1, first public 2026-10-13. https://arxiv.org/abs/2610.18802 . Especially Sections 1.1 and 1.4.

[3] B. Cloez and M.-N. Thai, *Fleming–Viot processes: two explicit examples*, arXiv:1603.04670, first public 2016-03-15. https://arxiv.org/abs/1603.04670 . Section 2 treats uniform killing.

[4] J. Corujo, *Dynamics of a Fleming–Viot type particle system on the cycle graph*, arXiv:2001.08000, first public 2020-01-22. https://arxiv.org/abs/2001.08000 . Section 1 and model assumptions (uniform killing).
