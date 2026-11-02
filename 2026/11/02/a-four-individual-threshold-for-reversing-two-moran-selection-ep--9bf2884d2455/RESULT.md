# A four-individual threshold for reversing two Moran selection epochs

## Finding

Consider the mutation-free, discrete-time, well-mixed, haploid Moran birth–death process with population size \(N\ge2\), in which each update selects a parent proportional to type fitness, then independently selects a uniformly random individual to replace (possibly the parent). At initial mutant count \(k\in\{1,\ldots,N-1\}\), compare exactly one update at mutant relative fitness \(a\), followed by one update at fitness \(b\), with the reversed order, where \(a>b>0\). Write \(K_2^{a,b}\) and \(K_2^{b,a}\) for the final mutant counts, respectively, and \(\Delta_{N,k}(a,b)=\mathbb E[K_2^{a,b}]-\mathbb E[K_2^{b,a}]\).

**Theorem (sharp smallest-population crossover).** For all \(a>b>0\), every interior initial count in populations \(N=2\) and \(N=3\) satisfies \(\Delta_{N,k}(a,b)>0\). For \(N=4\), this remains true at \(k=1\) and \(k=3\), but the exact central-state difference is

\[
\Delta_{4,2}(a,b)=\frac{(a-b)P(a,b)}{4(a+1)(a+3)(3a+1)(b+1)(b+3)(3b+1)},
\]

where

\[
P(a,b)=3a^2b^2+6a^2b-9a^2+6ab^2+116ab+6a-9b^2+6b+3.
\]

If both relative fitnesses are on the same side of neutrality, so that either \(a\ge b\ge1\) or \(1\ge a>b>0\), then \(\Delta_{4,2}(a,b)>0\). If \(a>1>b>0\), there is one and only one \(b_*(a)\in(0,1)\) satisfying

\[
3(a-1)(a+3)b_*^2+(6a^2+116a+6)b_*-3(a-1)(3a+1)=0.
\]

The stronger-first order is worse in expected mutant count exactly when \(0<b<b_*(a)\), better exactly when \(b_*(a)<b<1\), and tied at equality. Consequently, four is the smallest finite Moran population that can reverse the sign of a stronger-first two-update effect.

At \(a=5\), the sharp threshold is \(b_*(5)=(-23+\sqrt{601})/6\). For \(b=1/5\), the two expected mutant counts starting at \(k=2\) are \(383/192\) for strong-first and \(385/192\) for weak-first, so \(\Delta_{4,2}(5,1/5)=-1/96\). For \(b=1/2\), the gap is \(+5/224\). These two exact outcomes straddle the unique threshold.

## Assumptions and scope

The mutant carries fitness \(w>0\), and wild types carry fitness one. There is no mutation, migration, frequency-dependent fitness, spatial restriction, or environmental randomness beyond the deterministic choice of the two successive fitness values. An update includes self-replacement. The counts \(0\) and \(N\) are absorbing. Only the terminal expected count after exactly two elementary birth–death updates is compared; a 'generation' consisting of several updates is not covered by substituting its duration into these formulas. Strict inequality assumes \(a>b>0\) and an interior initial count. The result is a complete classification for populations up to four individuals, not for larger populations or for fixation probabilities.

For \(1\le j\le N-1\), the one-update probabilities of a mutant-count gain or loss are

\[
u_j(w)=\frac{j(N-j)w}{N(jw+N-j)},\qquad d_j(w)=\frac{j(N-j)}{N(jw+N-j)}.
\]

The remaining probability is \(1-u_j(w)-d_j(w)\). At absorbing boundaries set \(u_j=d_j=0\).

## Proof

Let \(g_w(j)=u_j(w)-d_j(w)=j(N-j)(w-1)/[N(jw+N-j)]\), extending it by zero to \(j=0,N\). If the first fitness is \(a\), after the first update the expected count is \(k+g_a(k)\), and after the second its additional expected drift is

\[
\mathbb E[g_b(K_1)]=g_b(k)+u_k(a)[g_b(k+1)-g_b(k)]+d_k(a)[g_b(k-1)-g_b(k)].
\]

Subtracting the reversed order cancels \(g_a(k)+g_b(k)\) and gives the **exact two-epoch commutator**

\[
\begin{aligned}
\Delta_{N,k}(a,b)={}&u_k(a)[g_b(k+1)-g_b(k)]-u_k(b)[g_a(k+1)-g_a(k)]\\
&+d_k(a)[g_b(k-1)-g_b(k)]-d_k(b)[g_a(k-1)-g_a(k)].
\end{aligned}
\]

Algebraic simplification for all interior states at \(N=2,3,4\) gives the following complete list. Every omitted numerator factor and denominator below is strictly positive for \(a>b>0\):

\[
\begin{aligned}
\Delta_{2,1}&=\frac{a-b}{2(a+1)(b+1)},\\
\Delta_{3,1}&=\frac{4ab(a-b)}{(a+2)(2a+1)(b+2)(2b+1)},\\
\Delta_{3,2}&=\frac{4(a-b)}{(a+2)(2a+1)(b+2)(2b+1)},\\
\Delta_{4,1}&=\frac{3ab(a-b)}{2(a+1)(a+3)(b+1)(b+3)},\\
\Delta_{4,2}&=\frac{(a-b)P(a,b)}{4(a+1)(a+3)(3a+1)(b+1)(b+3)(3b+1)},\\
\Delta_{4,3}&=\frac{3(a-b)}{2(a+1)(3a+1)(b+1)(3b+1)}.
\end{aligned}
\]

To classify the only potentially negative case, put

\[
H(x,y)=3x^2y^2+12x^2y+12xy^2+152xy+128x+128y+128>0\qquad(x,y\ge0).
\]

Direct expansion shows \(P(1+x,1+y)=H(x,y)\) and \(P((1+x)^{-1},(1+y)^{-1})=H(x,y)/[(1+x)^2(1+y)^2]\), proving positivity when both fitness values lie on the same side of one (including its boundary). If \(a>1>b\), writing \(P\) as a quadratic in \(b\) yields

\[
P(a,b)=3(a-1)(a+3)b^2+(6a^2+116a+6)b-3(a-1)(3a+1).
\]

Its derivative with respect to \(b\) is strictly positive for \(b>0\). Moreover, \(P(a,0)=-3(a-1)(3a+1)<0\) and \(P(a,1)=128a>0\). Continuity and strict monotonicity give the unique root in \((0,1)\) and the asserted two signs. The explicit other-state formulas prove minimality of four. Substitution \(a=5\) gives \(P(5,b)=32(3b^2+23b-6)\) and the claimed exact witness values. This proves the theorem.

## Verification

The supplied `moran_epoch_checker.py`, using symbolic algebra and independently implemented exact rational transition matrices, checks all six rational identities, the polynomial positivity transformations, the threshold polynomial, and the two sample comparisons. With SymPy 1.14.0 the saved checker reports 498 passed symbolic/rational checks. The proof itself is the displayed analytic derivation and strict sign classification; finite test points are not relied on to prove universal inequalities.

To reproduce: install the version in `requirements.txt`, then run `python moran_epoch_checker.py` from the extracted package directory.

## Relationship to prior work

The classical Moran model and its selection/fixation theory are established. Kluth and Baake (2013) treat a continuous-time, constant-fitness Moran model and ancestral/fixation quantities. Ashcroft, Altrock, and Galla (2014) analyze general finite birth–death dynamics in randomly switching environments, deriving fixation probabilities, fixation times, and stationary distributions; their framework can represent the transition kernels used here, but does not state the deterministic two-update mean-order sign or its smallest-population/unique-root classification. Dean, Lehman, and Yi (2017) discuss fluctuating selection and a Moran transition rule with the same single-step structure, emphasizing polymorphism, fixation, and evolution under fluctuating environments rather than this precise terminal two-step comparison. The contribution asserted here is limited to the exact six-case commutator classification, the minimal four-individual reversal, and its unique selection-strength threshold; it is not a new Moran model or a general theory of changing environments.

## Limitations

Results are algebraic and specific to independent uniform replacement (including self-replacement), fixed population size, exactly two single updates, and expectation of the terminal mutant count. They do not show a similar reversal for the probability of eventual fixation, a finite number of full generations, more than two epochs, or population sizes beyond four. The threshold should not be interpreted as an empirical rule for applying changing selective pressures. Earlier general work on stochastic ordering of selection kernels could conceivably imply the special case; a comprehensive historical priority audit has not been performed.

## References

1. Kluth, S., and Baake, E. (2013). *The Moran model with selection: Fixation probabilities, ancestral lines, and an alternative particle representation*. arXiv:1306.2772, first publicly submitted 2013-06-12. https://arxiv.org/abs/1306.2772
2. Ashcroft, P., Altrock, P. M., and Galla, T. (2014). *Fixation in finite populations evolving in fluctuating environments*. arXiv:1406.5619, first submitted 2014-06-21. https://arxiv.org/abs/1406.5619
3. Dean, A. M., Lehman, C., and Yi, X. (2017). *Fluctuating Selection in the Moran*. Genetics 205, 1271–1283. https://pmc.ncbi.nlm.nih.gov/articles/PMC5340338/
