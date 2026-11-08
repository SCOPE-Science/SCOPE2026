# A common rotation and exact joint frequencies for the Fibonacci and Lucas words

## Finding

Let \(\varphi=(1+\sqrt5)/2\) and \(\gamma=(5-\sqrt5)/10=1/(\varphi+2)\). Let \(f=f_0f_1\cdots\) be the Fibonacci word beginning \(010010100\cdots\), the fixed point of \(0\mapsto01\), \(1\mapsto0\). Let \(\ell=\ell_0\ell_1\cdots\) be Kimberling's Lucas word, obtained by replacing each \(1\) in \(f\) with \(11\) and leaving each \(0\) unchanged. These are OEIS A003849 and A383422, respectively.

For every integer \(n\ge0\), put \(t_n=\{(n+1)\gamma\}\), where braces denote fractional part. The **simultaneous rotation coding** is
\[
 f_n=1\ \Longleftrightarrow\ \{5t_n\}>2-5\gamma,
 \qquad
 \ell_n=1\ \Longleftrightarrow\ t_n>1-2\gamma.
\]
In particular the joined four-letter word \((f_n,\ell_n)\) is a coding of one circle rotation \(t\mapsto\{t+\gamma\}\).

Define \(N_{ab}(X)=\#\{0\le n<X:(f_n,\ell_n)=(a,b)\}\) for integers \(X\ge1\) and \(a,b\in\{0,1\}\). All four natural densities exist, and in the order \(00,01,10,11\) they are
\[
\boxed{\begin{aligned}
d_{00}&=\frac75-4\gamma,&d_{01}&=\frac35-\gamma,\\
d_{10}&=2\gamma-\frac25,&d_{11}&=3\gamma-\frac35.
\end{aligned}}
\]
More precisely \(N_{ab}(X)=Xd_{ab}+O(\log(X+2))\), with one absolute implied constant valid for all four pairs. In particular the equality-position sequence A383427 has density
\[
 d_{00}+d_{11}=\frac45-\gamma,
\]
and the two letters have strictly positive covariance
\[
 d_{11}-(d_{10}+d_{11})(d_{01}+d_{11})
 =\frac{5\sqrt5-11}{10}>0.
\]

**All finite-block version.** For every fixed integer \(h\ge1\) and every word \(w\) of \(h\) symbols from \(\{00,01,10,11\}\), its occurrence density exists, belongs to \(\mathbb Q(\sqrt5)\), and is effectively computable as the total length of a finite union of intervals. The count of its occurrences at starting positions \(0\le n<X\) equals that density times \(X\), with error \(O_h(\log(X+2))\).

## Assumptions and scope

Positions start at zero. The name “Lucas word” refers specifically to the OEIS A383422 word \(011001101\cdots\), not to a generic word formed from Lucas numbers. A word at position \(n\) is compared with the other word at **the same index** \(n\), even though their morphic source blocks have different lengths. The density is the ordinary limit over starting positions \(0,\ldots,X-1\), not a logarithmic or weighted density. Constants in \(O_h\) may depend on the fixed block length but never on \(X\).

The standard Fibonacci-word Beatty identity used below is the known formula: the \(k\)-th \(1\) of \(f\), for \(k\ge1\), lies at index \(\lfloor k\varphi^2\rfloor-1\). It is also the standard mechanical-word identity \(f_n=\lfloor(n+2)\varphi^{-2}\rfloor-\lfloor(n+1)\varphi^{-2}\rfloor\).

## Proof

**1. Beatty membership.** For any irrational \(\lambda>1\), write \(\alpha=1/\lambda\). An integer \(m\ge1\) belongs to \(\{\lfloor k\lambda\rfloor:k\ge1\}\) if and only if
\[
 \lfloor(m+1)\alpha\rfloor-\lfloor m\alpha\rfloor=1,
\]
equivalently \(\{m\alpha\}>1-\alpha\). Indeed the difference counts integers in \([m\alpha,(m+1)\alpha)\), an interval shorter than one. All inequalities here and below can be taken strict because the relevant orbit points cannot hit the stated endpoints.

**2. Fibonacci positions.** The standard Beatty identity for \(f\), applied with \(m=n+1\) and \(\alpha=\varphi^{-2}\), gives
\[
 f_n=1\iff\{(n+1)\varphi^{-2}\}>1-\varphi^{-2}.
\]
The identities \(\varphi^{-2}=5\gamma-1\) and \(1-\varphi^{-2}=2-5\gamma\) therefore give \(f_n=1\iff\{5t_n\}>2-5\gamma\).

**3. Lucas positions.** Let \(i_k=\lfloor k\varphi^2\rfloor-1\) denote the position of the \(k\)-th \(1\) of \(f\). Precisely \(k-1\) earlier \(1\)'s have been doubled, so the two positions of the corresponding \(11\) block in \(\ell\) are
\[
i_k+k-1=\lfloor k(\varphi+2)\rfloor-2,\qquad
i_k+k=\lfloor k(\varphi+2)\rfloor-1.
\]
Set \(\lambda=\varphi+2\) and \(\gamma=1/\lambda\). At an index \(n\), with \(m=n+1\), the Lucas letter equals one exactly when \(m\) or \(m+1\) belongs to the Beatty sequence of slope \(\lambda\). By Step 1 these conditions are, respectively, \(\{m\gamma\}>1-\gamma\) or \(\{(m+1)\gamma\}>1-\gamma\). Since \(0<\gamma<1/3\), their disjoint union is
\[
 \{m\gamma\}>1-2\gamma.
\]
This proves both simultaneous coding identities.

**4. Interval computation.** Put \(I=\{t\in[0,1):\{5t\}>2-5\gamma\}\) and \(J=(1-2\gamma,1)\). The first set is a disjoint union of five intervals
\[
 I_j=\left(\frac{j+2}{5}-\gamma,\frac{j+1}{5}\right),
 \qquad j=0,1,2,3,4,
\]
each of length \(\gamma-\frac15\). The left endpoint \(1-2\gamma\) of \(J\) lies between \(2/5\) and \(4/5-\gamma\); consequently \(I_0,I_1\) are disjoint from \(J\), and \(I_2,I_3,I_4\) are contained in \(J\). Thus the measures of \(I\cap J\), \(I\setminus J\), \(J\setminus I\), and \([0,1)\setminus(I\cup J)\) are
\[
3(\gamma-\tfrac15),\qquad
2(\gamma-\tfrac15),\qquad
2\gamma-3(\gamma-\tfrac15),\qquad
1-2\gamma-2(\gamma-\tfrac15).
\]
Assigning the appropriate \(11,10,01,00\) labels gives the claimed four values. Their sum is one, and the covariance formula follows by direct substitution together with \(5\gamma^2-5\gamma+1=0\).

**5. Frequencies and effective error.** The irrational rotation \(t_{n+1}=\{t_n+\gamma\}\) is equidistributed, so its visits to each of these finite unions of intervals have frequency equal to interval length. For the stronger error estimate, the continued fraction of \(\gamma\) is \([0;3,1,1,1,\ldots]\). If \(p_j/q_j\) is a convergent, then in any block of \(q_j\) rotation points each point differs, modulo one, by at most \(1/q_j\) from a translated uniform \(q_j\)-point grid. Hence the number of visits to each fixed interval during such a block differs from \(q_j\) times its length by an absolute constant. The bounded continued-fraction quotients allow any \(X\) to be decomposed into \(O(\log(X+2))\) such blocks (greedy denominators, using at most three of any size). Summing the errors proves \(O(\log(X+2))\) for each of the four interval unions.

For a prescribed length-\(h\) joined word \(w\), the allowed initial rotation phases are the intersection, over \(r=0,\ldots,h-1\), of the letter region for \(w_r\) shifted by \(-r\gamma\) modulo one. This is a finite union of intervals whose endpoints lie in \(\mathbb Q(\sqrt5)\); hence its measure is in that field and is computable by sorting and intersecting those endpoints. Apply the same convergent-grid discrepancy argument to this finite union to obtain the stated \(O_h(\log(X+2))\) error.

## Verification

The accompanying standalone `verify.py` uses Python standard-library integer square roots to compute exact Beatty positions, independently constructs the words from their defining substitution/concatenation recurrences, and compares the first 50,000 positions. It also checks the simultaneous rotation coding at 90-decimal-digit precision and compares the observed joint counts to the four predicted densities at several prefix lengths. The final observed joint counts in the order \(00,01,10,11\) at \(X=50000\) were \(14724,16178,7637,11461\), with maximum absolute density-count error below \(2.641\).

These are finite corroborating tests. They do not replace the general Beatty, interval, and irrational-rotation arguments above.

## Relationship to prior work

Alex Ashburn, *Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words*, arXiv:2610.04842v1 (public 2026-10-04), proves Clark Kimberling's conjectures about possible **gaps** between the four joint letter-position sequences and their equality set (Section 5). The definitions and gap results are prior work, not part of the novelty claim here. OEIS A383423, A383424, A383425, A383426 and A383427 record the corresponding positions and gap questions.

The Fibonacci mechanical-word and Beatty formulas, as well as equidistribution and logarithmic discrepancy for bounded-type irrational rotations, are classical and are not claimed as new. The assessed addition is an explicit **synchronization** of this particular non-uniformly expanded Lucas word with the Fibonacci word in one rotation, together with the four exact joint densities, positive covariance, and algorithmic finite-block frequency law. Searches of directly relevant recorded sequences, the motivating paper, accessible related literature, and publicly indexed mathematical findings did not identify a theorem covering this exact joint coding and frequency statement. This search does not certify historical priority.

## Limitations

The formula is specific to the indicated Fibonacci/Lucas word pair and to aligned zero-based indices. It does not assert identical densities for unrelated Lucas words, other morphic inflations, or shifted alignments. The logarithmic counting error is an order bound, not an optimal discrepancy constant. For general finite blocks, the result provides an effective interval-intersection algorithm but no precomputed table of every block frequency. Independent validation and a complete historical-priority audit have not been performed.

## References

1. A. Ashburn, *Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words*, arXiv:2610.04842v1, https://arxiv.org/abs/2610.04842 (first posted 2026-10-04 UTC).
2. OEIS A003849, *Infinite Fibonacci word*, https://oeis.org/A003849.
3. OEIS A383422, *Infinite Lucas word*, https://oeis.org/A383422.
4. OEIS A383423, A383424, A383425, A383426, *The four aligned letter-position sequences*, https://oeis.org/A383423, https://oeis.org/A383424, https://oeis.org/A383425, https://oeis.org/A383426.
5. OEIS A383427, *Equality positions of the two words*, https://oeis.org/A383427.
6. J. Peltomäki, *Abelian periods of factors of Sturmian words*, arXiv:1905.06138, https://arxiv.org/abs/1905.06138 (general background on Sturmian rotation codings, not this joint computation).
