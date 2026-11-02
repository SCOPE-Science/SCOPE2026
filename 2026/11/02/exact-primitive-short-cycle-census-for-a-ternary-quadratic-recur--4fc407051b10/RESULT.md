# Exact primitive short-cycle census for a ternary quadratic recurrence

## Finding

For every integer \(k\ge2\), consider the bijection
\[
T_k(w_0,\ldots,w_{k-1})=(w_1,\ldots,w_{k-1},\,w_0+w_{k-1}^2)
\]
on \((\mathbb Z/3\mathbb Z)^k\). Let \(d\) be any positive divisor of \(k\), put \(r\equiv k/d\pmod4\), and define
\[
F_k(d)=\begin{cases}
1,&r=0\text{ or }2,\\
1+4\displaystyle\sum_{\substack{0\le j\le d\\j\equiv3-d\ (\mathrm{mod}\ 4)}}\binom dj,&r=1,\\
1+4\displaystyle\sum_{\substack{0\le j\le d\\j\equiv3-2d\ (\mathrm{mod}\ 4)}}\binom dj,&r=3.
\end{cases}
\]
Then \(F_k(d)\) is **exactly** the number of states fixed by \(T_k^{4d}\). Every nonzero state fixed by \(T_k^{4k}\) has least period \(4d\) for some \(d\mid k\). The number of distinct cycles of least period exactly \(4d\) is
\[
\boxed{\mathcal C_k(4d)=\frac1{4d}\sum_{e\mid d}\mu(d/e)\bigl(F_k(e)-1\bigr),}
\]
where \(\mu\) is the classical Möbius function. The only additional cycle with period dividing \(4k\) is the fixed zero state.

Consequently, if \(k=2^a\ge4\), **every** nonzero state fixed by \(T_k^{4k}\) has least period exactly \(4k\): there are precisely \(2^k\) such states and \(2^k/(4k)\) such cycles. Nontrivial proper short cycles also occur: at \(k=9\) there is one cycle of length \(12\) and thirteen of length \(36\); at \(k=10\), one of length \(8\) and twenty-seven of length \(40\); at \(k=12\), one of length \(16\) and eighty-five of length \(48\).

## Assumptions and scope

All state coordinates and recurrence equations are taken modulo three. A cycle's least period is the least positive iteration count returning any, and therefore every, point of the cycle. The formulas hold for every \(k\ge2\), for every positive divisor \(d\mid k\), without any assumption that the initial state is sparse. They classify only cycles whose least periods divide \(4k\); longer cycles may exist and are not enumerated.

## Proof

**Step 1: period reduction.** The map \(T_k\) is bijective: from its image one recovers \(w_0\) by subtracting the square of the original final entry \(w_{k-1}\) (now the penultimate output coordinate) from the output's final coordinate. Thus a state fixed by \(T_k^{4d}\) corresponds bijectively to a bi-infinite \(4d\)-periodic word \((x_n)\) satisfying
\[
x_n-x_{n-k}=b_{n-1},\qquad b_n=[x_n\ne0]\in\{0,1\}.
\]
Here \(x_{n-1}^2=b_{n-1}\) in \(\mathbb F_3\). Put \(q=k/d\), \(r=q\pmod4\), and arrange the word into \(d\) columns of four entries \(x_{j,t}=x_{j+td}\), \(0\le j<d\), \(t\in\mathbb Z/4\mathbb Z\). For \(j>0\), the recurrence becomes
\[
x_{j,t}-x_{j,t-r}=b_{j-1,t};
\]
for \(j=0\), its right side is \(b_{d-1,t-1}\), with one additional row shift at the cyclic boundary.

**Step 2: even delay ratios.** If \(r=0\), the left side vanishes, forcing all \(b\)'s to vanish and hence the zero word. If \(r=2\), add the equations at rows \(t\) and \(t-2\). The left sides cancel, leaving \(b_{j-1,t}+b_{j-1,t-2}=0\) modulo three, with the analogous shifted indices at \(j=0\). Since both indicators are in \(\{0,1\}\), both vanish. Again the only word is zero. Hence \(F_k(d)=1\) in both cases.

**Step 3: odd delay ratios and one-zero columns.** If \(r=1\) or \(r=3\), summing the four row equations for each fixed column gives that the preceding column has \(0\) or \(3\) nonzero entries; it cannot have four. An all-zero column forces the following column to be constant (the row-difference equations have zero right sides and \(r\) is odd); a nonzero constant would have four nonzero entries, which is impossible. Iterating, an all-zero column forces the entire word to vanish. Thus every nonzero periodic word has **exactly one zero per column**.

Given the preceding column's zero row \(u\), there are exactly two ways to fill the next one-zero column. For \(r=1\), writing its entry in row \(u\) as \(a\), the values in rows \(u,u+1,u+2,u+3\) are \(a,a+1,a+2,a\) modulo three. Exactly one zero requires \(a=1\) or \(a=2\), locating the next zero at row \(u+2\) or \(u+1\), respectively. Therefore each ordinary column transition advances the zero row by \(1\) or \(2\). For \(r=3\), the corresponding values are \(a,a,a-1,a-2\); the next zero row advances by \(2\) or \(3\). At the transition across column \(d-1\) to column \(0\) the preceding column's indicator acquires an additional row shift of \(1\).

For \(r=1\), choose the initial zero row in four ways and the \(d\) successive row increments to be \(1\) or \(2\), with \(j\) increments of the larger type. Closure requires \(d+j+1\equiv0\pmod4\), or \(j\equiv3-d\pmod4\). For \(r=3\), use increments \(2\) or \(3\): closure is \(2d+j+1\equiv0\pmod4\). Every permitted choice fills the columns uniquely and satisfies the recurrence, and different choices give different words. Consequently the two binomial sums in \(F_k(d)\) count *all* nonzero words; adding the zero word completes the fixed-point formula.

**Step 4: possible least periods and Möbius inversion.** Apply Step 3 with \(d=k\), where \(r=1\). Every nonzero \(T_k^{4k}\)-fixed state has exactly one zero in each of the \(k\) columns and therefore exactly \(k\) zeros per \(4k\)-period. If its least period is \(m\mid4k\), its basic period has \(km/(4k)=m/4\) zeros, an integer. Thus \(4\mid m\), so \(m=4d\) for a divisor \(d\mid k\). Let \(P_k(d)\) count nonzero points with least period \(4d\). Then
\[
F_k(d)-1=\sum_{e\mid d}P_k(e),
\qquad
P_k(d)=\sum_{e\mid d}\mu(d/e)(F_k(e)-1).
\]
Each cycle of period \(4d\) consists of exactly \(4d\) states, proving the displayed formula for \(\mathcal C_k(4d)\).

**Step 5: powers of two.** Let \(k=2^a\ge4\). For each proper divisor \(d<k\), the ratio \(k/d\) is even, hence \(F_k(d)=1\) and \(P_k(d)=0\). For \(d=k\), the number of nonzero fixed states is
\[
4\sum_{j\equiv3-k\ (\mathrm{mod}\ 4)}\binom kj=2^k.
\]
The last equality follows from the fourth-roots-of-unity filter: since \(4\mid k\), the binomial sum in residue class \(3\pmod4\) equals \(2^{k-2}\), because \((1+i)^k\) is real for \(4\mid k\). Thus all \(2^k\) nonzero short-period states have least period \(4k\), giving \(2^k/(4k)\) distinct cycles.

## Verification

A standalone C++17 program `verify.cpp` performs exact, independent direct state iteration for every \(k\) between \(2\) and \(12\). For every divisor \(d\mid k\), it compares the fixed-point count at \(4d\) with the binomial formula, and compares the observed primitive periods with the Möbius-inverted formula, including cycle-integrality checks. Its successful output is:

`VERIFY_OK k_range=2..12 divisor_fixed_and_primitive_checks=34 states_examined=797157 short_orbits_total=195`

Compile and run with `g++ -std=c++17 -O3 verify.cpp -o verify && ./verify`. This is a finite consistency test. The uniform proof for all \(k\) rests on the four-column-row argument above, not on exhaustive enumeration.

## Relationship to prior work

Steven Finch, *Three Quadratic Recurrences Modulo 3: What We Can Prove and What We Can Guess* (first submitted October 25, 2026), Proposition 7 and Theorem 8, establishes permutation dynamics and counts states fixed by \(T_k^{4k}\). The present theorem agrees with that count when \(d=k\), but resolves the finer problem of **all primitive cycles of every length dividing \(4k\)**, including the previously uncounted proper periods \(4d\). Crucially, the new case \(k/d\equiv3\pmod4\) and the exclusion of even delay ratios supply fixed counts unavailable from simply substituting \(d\) into Finch's \(4k\)-fixed-point theorem. Möbius inversion then gives a complete period census. Other quadratic recurrences and finite-field dynamical systems may admit related classical methods, but no implication establishing this exact census was identified in the checked literature.

## Limitations

This result is not a census of the full permutation \(T_k\): it says nothing about cycles whose lengths do not divide \(4k\), including the large cycles observed by Finch. The closed-form binomial sums can contain cancellations under Möbius inversion; their nonnegative integer quotients are certified by the orbit proof. The claim has undergone a self-review but no independent mathematical audit. A prior implicit computation or an inaccessible historical treatment cannot be excluded.

## References

1. Steven Finch, *Three Quadratic Recurrences Modulo 3: What We Can Prove and What We Can Guess*, arXiv:2610.34300v1 (2026-10-25), Section 3 (Proposition 7, Theorem 8, Corollary 9), https://arxiv.org/html/2610.34300v1 .
2. Julien Cassaigne and Steven R. Finch, *A Class of 1-Additive Sequences and Quadratic Recurrences*, Experimental Mathematics **4** (1995), 49–60. Archived issue index: https://www.maths.tcd.ie/EMIS/journals/EM/expmath/volumes/4/4.html . Historical related context; its full PostScript text was not available for this comparison.
