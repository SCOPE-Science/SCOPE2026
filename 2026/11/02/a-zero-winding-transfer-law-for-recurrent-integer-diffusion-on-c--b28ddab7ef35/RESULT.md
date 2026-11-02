# A zero-winding transfer law for recurrent integer diffusion on cycles

## Finding

For every labelled simple cycle \(C_n\), \(n\ge3\), synchronous integer sign-gradient diffusion has an exact finite transfer-matrix census of its primitive two-cycles modulo simultaneous translation of all chip values. The transfer alphabet consists of nine ordered pairs of adjacent edge signs, and one Laurent-polynomial constant term enforces the previously missing cyclic closure constraint.

Write \(\Sigma=\{-1,0,1\}\). Index the rows and columns of a \(9\times9\) matrix \(T(z)\) by ordered pairs in \(\Sigma^2\). All entries vanish except transitions \((a,b)\to(b,c)\), whose weights are

\[
W(a,b,c;z)=
\begin{cases}
1,&b=0\text{ and }a+c=0,\\
\displaystyle\sum_{q=1}^{1-b(a+c)}z^{bq},&b\in\{-1,1\},\\
0,&\text{otherwise}.
\end{cases}
\]

The sum is zero if its upper limit is less than one. Then the **exact number of distinct primitive two-cycle orbits** of length-two temporal dynamics, with vertex labels retained and modulo adding a common integer to every vertex, is

\[
\boxed{\displaystyle N_n=\frac{[z^0]\operatorname{tr}(T(z)^n)-1}{2}.}
\]

The unique fixed-point class is constant. Every recurrent state has adjacent chip-value difference of absolute size at most three; this bound is sharp for every \(n\ge4\), whereas the sharp bound on the triangle is two. Since every integer-diffusion trajectory on a finite graph eventually has period one or two [2], this enumerates every recurrent orbit of these cyclic systems, not just a subset.

The first values are:

| Cycle length | Recurrent classes of states \([z^0]\operatorname{tr}(T(z)^n)\) | Primitive two-cycle orbits \(N_n\) |
|:--:|--:|--:|
| 3 | 19 | 9 |
| 4 | 47 | 23 |
| 5 | 171 | 85 |
| 6 | 517 | 258 |
| 7 | 1793 | 896 |
| 8 | 5927 | 2963 |
| 9 | 20287 | 10143 |
| 10 | 69307 | 34653 |
| 11 | 238283 | 119141 |
| 12 | 823865 | 411932 |

## Assumptions and scope

The vertices of \(C_n\) are \(\mathbb Z/n\mathbb Z\), adjacent precisely when their indices differ by one cyclically, with \(n\ge3\). Configurations are arbitrary integer vectors \(x=(x_i)\). The synchronous update is

\[
F(x)_i=x_i+\operatorname{sgn}(x_{i-1}-x_i)+\operatorname{sgn}(x_{i+1}-x_i).
\]

The function \(\operatorname{sgn}\) takes values \(-1,0,1\), with ties giving zero. No total-chip or nonnegativity restriction is imposed: negative chip values are permitted. A *primitive two-cycle* is an unordered pair of distinct configurations \(\{x,F(x)\}\) with \(F^2(x)=x\), counted up to applying a single common integer translation to both configurations. Cyclic relabellings, spatial reflections and changes of the temporal phase beyond interchanging the two states are **not** imposed as equivalences. Each graph vertex remains labelled. Total chip count is preserved by \(F\).

## Proof

**1. Edge flux and zero divergence.** For an arbitrary periodic state of temporal period dividing two set

\[
e_i=x_{i+1}-x_i,\qquad s_i=\operatorname{sgn}(e_i),\qquad y=F(x),\qquad t_i=\operatorname{sgn}(y_{i+1}-y_i).
\]

The synchronous rule is \(y_i=x_i+s_i-s_{i-1}\). Thus \(F(y)=x\) means that \(s_i+t_i\) is independent of \(i\). Since \(\sum_i e_i=0\), a cyclic difference word cannot consist exclusively of strictly positive steps, nor exclusively of strictly negative steps, and an all-zero difference word cannot support a nonzero flux. If the common integer \(s_i+t_i\) were positive, each \(s_i\) would be nonnegative and at least one would be positive, contradicting \(\sum_i e_i=0\); a negative constant is ruled out analogously. Hence

\[t_i=-s_i\qquad\text{for every }i.\]

In particular the sign on each non-tied edge reverses over the update; a tied edge remains tied. Conversely these sign reversals imply \(F(y)=x\) because the two successive edge fluxes cancel.

**2. Exact local inequalities.** Taking differences gives

\[y_{i+1}-y_i=e_i+s_{i-1}-2s_i+s_{i+1}.\]

For \(s_i=0\), the edge difference is zero and remains zero exactly when \(s_{i-1}+s_{i+1}=0\). For \(s_i=b\in\{-1,1\}\), write \(e_i=bq_i\), with \(q_i\) a positive integer. The required opposite sign of the next edge difference is equivalent to

\[1\le q_i\le 1-b(s_{i-1}+s_{i+1}).\]

These inequalities are necessary and sufficient, provided the cyclic closure \(\sum_i e_i=0\) is imposed. Because the upper bound is at most three, every two-periodic state has edge gaps at most three in absolute value. The proof does not assume such a bound in advance.

**3. Transfer and zero winding.** A closed length-\(n\) walk among pair-states \((s_{i-1},s_i)\) in the matrix \(T(z)\) chooses precisely one admissible signed step \(e_i\) per cyclic position. The exponents add to \(\sum_i e_i\). Hence \([z^0]\operatorname{tr}(T(z)^n)\) counts exactly the sign-step words satisfying all local reversibility inequalities *and* global closure. A zero-sum edge word determines the original vector uniquely up to integer translation by fixing \(x_0=0\) and cumulatively summing its differences. The resulting vector is two-periodic by steps 1–2. This is a bijection, with neither overcounting nor omitted winding classes.

**4. Temporal orbit quotient.** A fixed vector satisfies \(s_i=s_{i-1}\) for all \(i\); the only cyclically realizable uniform sign is zero, so every fixed vector is constant and is one translation class. All other counted vectors have primitive period two. Their two phases are distinct even modulo translation: if \(F(x)=x+c\mathbf1\), preservation of the total chip sum implies \(nc=0\), hence \(c=0\), which would make \(x\) fixed. Therefore the non-fixed phase classes pair without fixed points, giving \((R_n-1)/2\) orbits for \(R_n=[z^0]\operatorname{tr}(T(z)^n)\).

**5. Sharp edge-gap boundary.** For every even \(n=2k\ge4\), the cyclic difference word

\[(-3,3,(-1,1)^{k-1})\]

where the parenthesized pair is repeated \(k-1\) times, satisfies the inequalities and has zero sum. For every odd \(n=2k+1\ge5\), the word

\[(-3,1,0,-1,3,(-1,1)^{k-2})\]

works likewise. These are legitimate primitive two-cycles of gap three. In the triangle, a putative gap of three would require both neighboring edge signs to be opposite; their gaps could each have magnitude only one, making zero sum impossible. The difference word \((-2,0,2)\) is a legitimate triangle two-cycle, proving that the sharp bound there is two.

**6. Exhaustiveness among recurrent periods.** The fact that every trajectory of finite-graph integer diffusion eventually becomes periodic with period at most two is the previously published theorem of Long and Narayanan [2]; its proof is not claimed here. The present steps classify and enumerate all the fixed and primitive two-periodic configurations specifically on cycles.

## Verification

Run `python3 verify_cycle_diff.py`. The standard-library program implements the nine-state transfer independently of the direct integer-update check. For every \(3\le n\le8\), it enumerates all cyclic integer difference sequences with each entry in \([-3,3]\) (using the already-proved bound), constructs one normalized vector per sequence and checks \(F^2(x)=x\). The direct counts coincide with transfer coefficients. The transfer coefficients are also evaluated for \(3\le n\le12\); explicit sharpness witnesses are checked directly for every \(3\le n\le20\).

The successful replay is preserved in `verification_output.txt`. Computational enumeration here verifies finite instances but is **not** used as a proof of the all-length statement; steps 1–5 provide the infinite-family argument.

## Relationship to prior work

Duffy, Lidbetter, Messinger and Nowakowski [1] introduced integer diffusion, treated paths and cycles dynamically, and proved an evolving edge-gap bound of three for degree-two neighbors. That local upper bound and the underlying update rule are **prior work**, not claimed as new. Long and Narayanan [2] proved general eventual period at most two and edge-reversal behavior. Mullen, Cox and Nowakowski [3] counted periodic configurations on **paths** and derived their recurrence. Their path count does not directly incorporate the mandatory zero-sum closure of the cyclic edge-difference word, nor does it state the nine-state Laurent transfer formula and its cycle values above. The result here adds the exact zero-winding orbit census for labelled simple cycles and shows sharpness of the recurrence-specific gap bound in every cyclic length.

## Limitations

This count is not a census at a fixed conserved total number of chips, nor a quotient by graph automorphisms. It does not enumerate transient basin sizes or capture times. General claims about *eventual* periods invoke [2]. Comparison against unindexed literature and unavailable extended sources can leave historical equivalence risk; no independent mathematical audit has been performed. The finite program is a consistency check, not a certificate for arbitrary length.

## References

[1] C. Duffy, T. F. Lidbetter, M. E. Messinger, R. J. Nowakowski, *A Variation on Chip-Firing: the diffusion game*, arXiv:1609.05792, first public 2016-09-19, https://arxiv.org/abs/1609.05792.

[2] J. Long, B. Narayanan, *Diffusion on graphs is eventually periodic*, arXiv:1704.04295, first public 2017-04-13, https://arxiv.org/abs/1704.04295.

[3] T. Mullen, D. Cox, R. J. Nowakowski, *Counting Path Configurations in Parallel Diffusion*, arXiv:2010.04750, first public 2020-10-09, https://arxiv.org/abs/2010.04750.
