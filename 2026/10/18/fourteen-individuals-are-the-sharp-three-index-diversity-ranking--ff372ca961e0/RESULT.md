# Fourteen individuals are the sharp three-index diversity-ranking reversal threshold

## Finding

For two finite communities with equal integer census size \(N\), write their positive species-abundance profiles as integer partitions \(A\) and \(B\) of \(N\). Let \(D_q\) denote Hill effective-species diversity of order \(q\), specifically richness \(D_0\), inverse Simpson concentration \(D_2\), and reciprocal Berger--Parker dominance \(D_\infty\).

**Theorem.** The strict ranking pattern
\[
D_0(A)<D_0(B),\qquad D_2(A)>D_2(B),\qquad D_\infty(A)<D_\infty(B)
\]
is impossible when \(N\le13\). For \(N=14\) it occurs for exactly one unordered pair of abundance partitions, up to interchanging the community labels:
\[
A=(6,2,2,2,2),\qquad B=(5,5,1,1,1,1).
\]
In that orientation, the triples of exact diversities are
\[
(D_0,D_2,D_\infty)(A)=\left(5,\frac{49}{13},\frac73\right),
\quad
(D_0,D_2,D_\infty)(B)=\left(6,\frac{98}{27},\frac{14}{5}\right).
\]
Thus the middle Hill order favors the community that both endpoint indices rank lower. Continuity of Hill diversity in its order implies at least two profile intersections for this pair. The sharp lower bound here concerns the **specific ordered triple** of orders \(0,2,\infty\), not arbitrary intersections or other choices of Hill orders.

## Assumptions and scope

A profile is a nonincreasing finite sequence \(a_1\ge\cdots\ge a_r\ge1\) of integers with total \(N\ge1\), regarded up to permuting species labels. Only equal-total community pairs are compared; there is no subsampling, ecological interaction, stochastic observation model, or correction for incomplete sampling. With \(p_i=a_i/N\), set
\[
D_0(a)=r,\qquad D_2(a)=\left(\sum_{i=1}^r p_i^2\right)^{-1}
=\frac{N^2}{\sum_i a_i^2},\qquad
D_\infty(a)=\frac{1}{\max_i p_i}=\frac{N}{a_1}.
\]
All inequalities are strict. The two comparisons at endpoint orders \(0\) and \(\infty\) must have the same direction, opposite to order \(2\). The named triple corresponds to standard richness, Hill--Simpson and reciprocal Berger--Parker measures, not to sampling-effort rarefaction.

## Proof

**1. Orientation and necessary conditions.** Orient any witness so that \(A\) has fewer species, with \(r=|A|<|B|\). Put \(x=\max A\), \(S(a)=\sum_i a_i^2\), and write \(N=\sum_i a_i\). The three strict Hill-index inequalities are exactly
\[
r<|B|,\qquad x>\max B,\qquad S(A)<S(B).
\]
The case \(r=1\) is impossible because then \(S(A)=N^2\ge S(B)\). Hence \(2\le r\le N-1\), \(2\le x\le N-r+1\), and all parts of \(B\) are at most \(c=x-1\).

**2. Sharp lower square-sum envelope for \(A\).** After fixing its largest part \(x\), minimize the remaining sum of squares by balancing the \(r-1\) other positive integer parts. Put
\[
t=\left\lfloor\frac{N-x}{r-1}\right\rfloor,\quad
u=N-x-(r-1)t.
\]
Provided \(1\le t\) and the balanced parts do not exceed \(x\), the exact lower bound is
\[
S(A)\ge L(N,r,x):=x^2+(r-1-u)t^2+u(t+1)^2.
\]
If a feasible \(A\) exists these conditions automatically hold. The smoothing identity \((u+1)^2+(v-1)^2-u^2-v^2=2(u-v+1)<0\) for \(v\ge u+2\) proves that balance minimizes the sum, with equality only for the indicated multiset.

**3. Sharp upper square-sum envelope for \(B\).** Since \(B\) has at least \(r+1\) positive parts, and every part is at most \(c\), it has at least
\[
s_0=\max\!\left(r+1,\left\lceil\frac{N}{c}\right\rceil\right)
\]
parts. Among all such profiles the most concentrated one has exactly \(s_0\) positive parts. Start with \(s_0\) ones and greedily allocate the \(N-s_0\) remaining units to the first coordinate up to \(c\), then to the next, etc. For every \(j\), its sum of the first \(j\) entries is \(\min(jc,N-(s_0-j))\); any competing profile has no larger first-\(j\) sum, because it has at least \(s_0-j\) other positive entries. It therefore majorizes every permissible \(B\), and strict convexity of squares gives the sharp upper bound \(S(B)\le U(N,s_0,c)\), with equality only for the greedy multiset.

For \(c=1\), \(U=N\). For \(c\ge2\), set \(h=\lfloor(N-s_0)/(c-1)\rfloor\), \(v=N-s_0-h(c-1)\). Explicitly,
\[
U=\begin{cases}
hc^2+s_0-h,&v=0,\\
hc^2+(1+v)^2+s_0-h-1,&1\le v<c-1.
\end{cases}
\]
These are exact integer formulas, not numerical relaxations.

**4. Finite sharp cutoff certificate.** Any witness must satisfy \(L(N,r,x)<U(N,s_0,x-1)\). The standalone program `verify_hill.py` uses the displayed integer formulas, testing every
\[
1\le N\le14,\quad 2\le r\le N-1,\quad 2\le x\le N-r+1
\]
with feasible balanced profiles. Its complete output of surviving parameters is exactly
\[
(N,r,x,s_0,L,U)=(14,5,6,6,52,54).
\]
Consequently no witness exists through census \(13\). This finite check is exhaustive by the proved envelopes, not by a heuristic search over illustrative examples.

**5. Uniqueness at the boundary.** Every integer square satisfies \(a^2\equiv a\pmod 2\), so \(S(A)\) and \(S(B)\) both have parity \(N\). At \(N=14\), the bounds \(52\le S(A)<S(B)\le54\) therefore force \(S(A)=52\) and \(S(B)=54\). The strict-convexity equality cases in steps 2 and 3 force respectively
\[
A=(6,2,2,2,2),\qquad B=(5,5,1,1,1,1).
\]
Conversely these profiles satisfy \(S(A)=52<54=S(B)\), \(r(A)=5<6=r(B)\), and \(\max A=6>5=\max B\). The displayed exact Hill diversities follow. This proves sharpness and the complete classification.

## Verification

Run `python3 verify_hill.py` with the standard library. The program independently generates every integer partition through \(N=14\) by descending-part recursion and by part-multiplicity recursion, checks agreement, and compares all \(20{,}283\) unordered partition pairs. The direct enumeration finds the unique stated witness. Separately, it evaluates both analytic square-sum envelopes for every admissible parameter, checks each against independent partition extrema, and reports the lone envelope candidate. It verifies the displayed rational comparisons and the parity argument exactly. A finite program certifies only the finite case \(N\le14\); the extremal-envelope proof is needed to justify the complete reduction.

## Relationship to prior work

Hill (1973) defined the effective-species diversity family. Patil and Taillie (1982) studied sensitivity of diversity rankings and crossing-point phenomena. Morris and colleagues (2014) explicitly present richness, inverse Simpson and reciprocal Berger--Parker on the common Hill-order scale. Roswell, Dushoff and Winfree (2021) discuss crossing diversity profiles and index choice, with full accessible article text and examples. Those formulations imply that different orders need not rank communities identically; they do **not in the material inspected** supply the integer minimal-census threshold or the unique boundary pair established here. This finding does not claim that diversity-profile crossings or Simpson/Berger--Parker disagreement are new in general.

## Limitations

The theorem concerns exact integer abundance profiles and three fixed diversity orders. It does not characterize all intersections of Hill curves, imply a sampling-coverage guarantee, or prescribe index choice for field surveys. Literature equivalence remains a bibliographic risk: the full Patil--Taillie paper (1982) and original full Hill article (1973) were not accessible for complete inspection. The accessible abstracts, the full Morris (2014) text, and the relevant full-text sections of Roswell et al. (2021) support the conceptual contrast but not proof of literature-wide absence. Independent audit has not been performed.

## References

- Hill, M. O. (1973). Diversity and Evenness: A Unifying Notation and Its Consequences. *Ecology* 54:427--432. https://doi.org/10.2307/1934352 (first public source date verified as 1973-03-01).
- Patil, G. P., and Taillie, C. (1982). Diversity as a Concept and its Measurement. *JASA* 77:548--561. https://doi.org/10.1080/01621459.1982.10477845.
- Morris, E. K., et al. (2014). Choosing and using diversity indices: insights for ecological applications from the German Biodiversity Exploratories. *Ecology and Evolution*. https://doi.org/10.1002/ece3.1155.
- Roswell, M., Dushoff, J., and Winfree, R. (2021). A conceptual guide to measuring species diversity. *Oikos* 130:321--338. https://doi.org/10.1111/oik.07202.
