# Sharp fixed-content spectrum of cyclic binary two-binomial profiles

## Finding

For any positive integers \(p,q\), put \(N=p+q\), \(d=\gcd(p,q)\), and \(L=N/d\). For a binary word \(w\) having exactly \(p\) zeros and \(q\) ones, let \(C(w)\) denote the number of distinct equivalence classes among its \(N\) *indexed* cyclic rotations, where equivalence means equality of all scattered-subsequence counts of lengths one and two. Then

\[
\boxed{L\le C(w)\le N-d+1.}
\]

Every integer in this entire closed interval occurs for a word with the same prescribed \(p,q\). The lower equality holds precisely for words of the form \(w=u^d\), where \(u\) contains \(p/d\) zeros and \(q/d\) ones; the upper equality is attained by \(0^p1^q\).

A stronger exact recognition rule is also proved: for distinct starts \(i,j\) of cyclic rotations, their two-binomial profiles coincide if and only if the directed circular arc from \(i\) to \(j\) of length \(\ell\) has exactly \(\ell q/N\) ones. In particular, \(N\mid\ell q\) is necessary for a collision.

## Assumptions and scope

All words are finite over the ordered alphabet \(\{0,1\}\); \(p,q\) are both positive. The scattered-subsequence count \(\binom{v}{ab}\) is the number of ordered pairs of positions carrying symbols \(a,b\), without requiring adjacency. Each of the \(N\) rotations is indexed by its starting position, even when some resulting strings agree. The number \(C(w)\) counts equivalence classes, not multiplicities. A directed circular arc consists of the successive letters from its first start up to but not including its second; for the recognition rule take its length in \(\{1,\ldots,N-1\}\).

For a binary word with fixed \(p,q\), its entire two-binomial profile is determined by the one statistic \(F(v)=\binom{v}{01}\): the counts of all letters are fixed, \(\binom{v}{00}=\binom p2\), \(\binom{v}{11}=\binom q2\), and \(\binom{v}{10}=pq-F(v)\).

## Proof

**1. Height identity and the collision criterion.** Write \(\rho_i(w)\) for the rotation beginning at position \(i\), with positions numbered \(0,\ldots,N-1\). Put \(f_i=F(\rho_i(w))\). Moving a leading \(0\) to the end decreases \(F\) by \(q\), and moving a leading \(1\) to the end increases \(F\) by \(p\). Therefore, if \(B_i\) is the number of ones in the linear prefix of \(w\) of length \(i\),

\[
 f_i-f_0=NB_i-qi=:h_i,\qquad 0\le i\le N.
\]

Here \(h_0=h_N=0\), and the identity extends periodically to cyclic start indices. For starts \(i<j\), \(h_j-h_i=N(B_j-B_i)-q(j-i)\). Thus equality of their profiles is equivalent to the intervening arc having \((j-i)q/N\) ones. For the reverse circular arc the same property is equivalent by subtracting from the total \(q\).

**2. The lower bound and its equality case.** Since \(h_i\equiv-qi\pmod N\), equal heights require \(N\mid q(i-j)\), equivalently \(L\mid i-j\). Hence the \(L\) classes of indices modulo \(L\) give distinct heights and \(C(w)\ge L\). If \(C(w)=L\), all indices in each residue class modulo \(L\) must have equal heights; in particular \(h_{i+L}=h_i\) for each cyclic index \(i\). Differencing adjacent such equalities gives \(Nw_{i+L}-q=Nw_i-q\), so \(w_{i+L}=w_i\) everywhere. Thus \(w\) has period \(L\) and is \(u^d\). Conversely, for \(w=u^d\) with the indicated composition, each length-\(L\) arc contains exactly \(q/d\) ones, so \(h_{i+L}=h_i\), and exactly \(L\) heights occur.

**3. A balanced arc and the upper bound.** Assume \(d\ge2\). Let \(W_i\) count the ones in the cyclic window of length \(L\) beginning at \(i\). Summing over all \(N\) starts shows that their average equals \(Lq/N=q/d\), an integer. Consecutive \(W_i\) differ by at most one. If not every \(W_i\) equals their integer average, some are below and others above, and the step-by-one property forces an exact average. Therefore some length-\(L\) arc has \(q/d\) ones and height displacement zero.

Delete this arc and concatenate the remaining symbols into a circular word \(v\). Its composition is \(((d-1)p/d,(d-1)q/d)\), its length is \((d-1)L\), and its content gcd is exactly \(d-1\), because \(p/d\) and \(q/d\) are coprime. The original height walk and the shortened height walk have the same increments outside the deleted arc; the deleted arc begins and ends at the same height. Consequently all heights of \(v\) (after an irrelevant additive translation) also occur among those of \(w\), and the only potentially new distinct heights are the \(L-1\) internal heights of the deleted arc. Thus \(C(w)\le C(v)+L-1\). The base case \(d=1\) has at most \(N\) indexed rotations, agreeing with \(N-d+1\). Induction on \(d\) yields

\[
C(w)\le ((d-1)L-(d-1)+1)+(L-1)=dL-d+1=N-d+1.
\]

**4. Sharpness of the upper bound.** For \(w=0^p1^q\), the heights along its initial zeros are \(0,-q,-2q,\ldots,-pq\); after the ones they are \(-pq+p,-pq+2p,\ldots,-p\), omitting the final return to zero. Each progression is individually injective. Equality \(-aq=-pq+bp\) with \(0\le a\le p\) and \(1\le b\le q-1\) occurs for exactly \(d-1\) pairs, corresponding to the proper multiples of the primitive content ratio \((p/d,q/d)\). Hence the \(N\) starts give precisely \(N-(d-1)=N-d+1\) different heights.

**5. No gaps between the bounds.** Interchanging adjacent unequal symbols in a linear word changes exactly one prefix-one-count \(B_i\), hence exactly one height \(h_i\) among the \(N\) starts; every other height remains identical. Changing one entry in a finite multiset changes the number of distinct values by at most one. Thus \(C\) changes by at most one under an adjacent \(01\leftrightarrow10\) transposition. The graph of fixed-content binary words linked by such swaps is connected. Choose a path from the lower witness \(u^d\) to the upper witness \(0^p1^q\). An integer-valued sequence with steps of magnitude at most one that connects the two endpoint values necessarily attains every intermediate integer, completing the proof.

## Verification

The standalone script `checker.py` independently constructs all fixed-content cyclic rotations, explicitly counts scattered `01` pairs, and exhaustively checks the bounds, collision criterion, minimizer characterization, and attainment of every intermediate count across every binary word of lengths 2 through 14. It additionally checks canonical witnesses and the balanced-arc property for all 9,801 pairs of positive content parameters at most 99. The observed passing totals are 32,738 mixed binary words and 9,801 parameter pairs. These finite computations supplement, but do not replace, the unrestricted proof above.

Reproduce with `python3 checker.py` in a directory containing this `RESULT.md` and the checker. The proof does not depend on a software environment or a computational extrapolation.

## Relationship to prior work

Rigo and Salimov (2013) introduced binomial equivalence and related complexity. Lejeune, Rigo and Rosenfeld (2020) classified equivalence among finite words using Parikh matrices; those results motivate the reduction to a scattered `01` statistic but do not supply the fixed-content circular orbit spectrum stated here. Richomme (2025) studies binary two-binomial coefficients and fair words rather than this exact orbit cardinality range.

A particularly close **equivalent encoding** appears in Chuan (2004): its moment statistic \(M(v)=\sum_{j=1}^N (N+1-j)v_j\), for fixed \(p,q\), obeys \(M(v)=q(2N+1-q)/2-F(v)\). Hence the set of moments of conjugate words is an affine image of precisely the scattered-`01` rotation statistic in this theorem. The available abstract characterizes Christoffel-type extremizers of *moment spread* and consecutiveness, rather than the fixed-content interval of *numbers of distinct moments*. The complete Chuan paper was not accessible for theorem-by-theorem comparison: it could contain closely related or covering cardinality results. Historical originality is therefore qualified, not certified.

## Limitations

The complete range theorem is for binary words with both symbols present, equality of scattered subsequences of length at most two, and rotations of the whole finite word. The analogous problem for higher binomial orders or larger alphabets is not resolved. The proof is self-contained; the closest potentially covering original full text by Chuan (2004) remained inaccessible, leaving a significant historical priority risk. No independent mathematical validation has been performed.

## References

1. M. Rigo and P. Salimov (2013), *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, available 27 May 2013. https://orbi.uliege.be/handle/2268/149313
2. M. Lejeune, M. Rigo and M. Rosenfeld (2020), *On the binomial equivalence classes of finite words*. https://orbi.uliege.be/bitstream/2268/249124/1/LejeuneRigoRosenfeld-ijacVersion2.pdf
3. M. Richomme (2025), *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*. https://arxiv.org/pdf/2510.07159
4. W.-F. Chuan (2004), *Moments of conjugacy classes of binary words*, Theoretical Computer Science. https://doi.org/10.1016/S0304-3975(03)00398-0
