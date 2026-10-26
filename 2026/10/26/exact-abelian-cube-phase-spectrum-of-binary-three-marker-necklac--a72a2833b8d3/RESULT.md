# Exact Abelian-cube phase spectrum of binary three-marker necklaces

## Finding
For every integer \(p\ge1\), consider directed binary necklaces of circumference \(3p\) containing exactly three ones. A cyclic cut position \(s\) is *successful* if the three successive length-\(p\) blocks starting at \(s\) are Abelian equivalent, meaning that their numbers of ones (and therefore zeros) agree. As the whole circle has three ones, each successful block contains exactly one.

Let \(R(C)\) be the count of successful **indexed cut positions** modulo \(3p\). The clockwise distances \(d_1,d_2,d_3\) between successive ones are positive and sum to \(3p\). Put \(r=\min(d_1,d_2,d_3)\) and \(t=\max(d_1,d_2,d_3)\). Then
\[
 R(C)=3\max\{0,\min(r,2p-t)\}.
\]
Writing \(K(C)=R(C)/3\), the number \(C_{p,k}\) of directed necklaces with \(K(C)=k\) is exactly
\[
 C_{p,k}=\begin{cases}
 p(p-1)/2,&k=0,\\
 2(p-k),&1\le k<p,\\
 1,&k=p,\\
 0,&\text{otherwise}.
 \end{cases}
\]
Thus the total number of necklaces is \((3p^2-3p+2)/2\), the possible phase counts are precisely the multiples of three from zero through \(3p\), except that for \(p=1\) only three occurs. Among uniformly sampled necklaces, \(R(C)/(3p)\) converges in distribution to a variable \(X\) satisfying \(\Pr(X=0)=1/3\) and having density \(4(1-x)/3\) on \(0<x<1\); in particular \(\mathbb E[X]=2/9\).

## Assumptions and scope
The alphabet is \(\{0,1\}\). A directed necklace identifies cyclic rotations, **not** reversal. Markers are the three occurrences of one. The positive cyclic distances include the next marker position; their associated zero-gap lengths are \(d_i-1\). The rotation symmetry of the necklace does **not** identify indexed cut positions when counting \(R(C)\): a periodic word may produce the same rotated string at several distinct physical cuts. All counts are for integer \(p\ge1\), with the entire circular word partitioned into exactly three contiguous equal-length blocks.

## Proof
**Step 1: exact cut count.** Choose and label a first marker at position zero, with the next ones at positions \(d_1\) and \(d_1+d_2\) on the unwrapped interval of length \(3p\). Consider cuts in which these are the markers in blocks one, two, and three, respectively. The cut coordinate \(s\) must lie simultaneously in
\[
 [-p+1,0],\quad[d_1-2p+1,d_1-p],\quad[d_1+d_2-3p+1,d_1+d_2-2p].
\]
The number of integers in this intersection is
\[
 H=\max\bigl\{0,p-\operatorname{span}\{0,d_1-p,d_1+d_2-2p\}\bigr\},
\]
where \(\operatorname{span}\) denotes largest minus smallest. Since \(d_1+d_2-2p=p-d_3\), the three pairwise distances between the displayed entries are \(|d_1-p|\), \(|d_2-p|\), and \(|d_3-p|\). Hence
\[
 H=\max\{0,p-\max_i|d_i-p|\}=\max\{0,\min(r,2p-t)\}.
\]
The successful cuts partition uniquely into three disjoint classes according to which of the three markers appears in the first block. Cycling the marker labels does not change the span; each class therefore has size \(H\). This proves \(R(C)=3H\), including all degenerate and periodic cases.

**Step 2: count the superlevel sets.** Fix an integer \(k\) with \(1\le k\le p\). The inequality \(K(C)\ge k\) is equivalent to all three distances lying in the integer interval \([k,2p-k]\). Put \(q=p-k\) and \(e_i=d_i-k\). These constraints become
\[
 e_1+e_2+e_3=3q,\qquad0\le e_i\le2q.
\]
There are \(\binom{3q+2}{2}\) nonnegative solutions without the upper bounds. For each of the three indices, solutions violating its upper bound number \(\binom{q+1}{2}\), and no two violations can occur simultaneously. Thus the number of *ordered* feasible triples equals
\[
 N_q=\binom{3q+2}{2}-3\binom{q+1}{2}=3q(q+1)+1.
\]
These triples represent directed necklaces modulo cyclic permutations of the three entries. This action of a cyclic group of order three has exactly one fixed point, \((q,q,q)\), under either nontrivial rotation. Burnside's lemma yields the number of necklaces with \(K(C)\ge k\):
\[
 B_k=(N_q+2)/3=q(q+1)+1=(p-k)(p-k+1)+1.
\]
Consequently, for \(1\le k<p\), the number with \(K(C)=k\) is \(B_k-B_{k+1}=2(p-k)\), and the number with \(K(C)=p\) is \(B_p=1\).

**Step 3: zero phase count and complete spectrum.** All positive triples of sum \(3p\) number \(\binom{3p-1}{2}\) in ordered form; exactly \((p,p,p)\) is fixed by a nontrivial cyclic permutation. Hence there are
\[
 T_p=\frac{\binom{3p-1}{2}+2}{3}=\frac{3p^2-3p+2}{2}
\]
necklaces in total, and those with no successful phase number
\[
 C_{p,0}=T_p-B_1=\frac{p(p-1)}2.
\]
All formulas remain valid at \(p=1\), where the singleton necklace has three indexed successful cuts.

**Step 4: limiting law.** For a uniformly selected necklace, the mass at zero is \(p(p-1)/(3p^2-3p+2)\), which tends to \(1/3\). For \(1\le k<p\), the mass at \(K/p=k/p\) equals \(2(p-k)/T_p\). For every bounded continuous function \(f\), the Riemann sums converge:
\[
 \frac1{T_p}\sum_{k=1}^{p-1}2(p-k)f(k/p)
 \longrightarrow \int_0^1 \frac{4(1-x)}3f(x)\,dx.
\]
The remaining maximal class has mass \(1/T_p\to0\). This proves convergence to the asserted mixed law; integrating \(x\cdot4(1-x)/3\) gives its mean \(2/9\).

## Verification
A standalone standard-library Python program, `checker.py`, directly enumerates every labeled three-one support in circles of length \(3p\) for \(1\le p\le12\), evaluating all \(3p\) cyclic cuts without using the gap formula. It compares the result against the formula for all \(24{,}531\) supports. Separately, it enumerates ordered positive distance triples and their cyclic orbits and checks the complete class-size distribution for every \(1\le p\le120\). These finite checks passed; the proof above, not the finite observations, supplies the unrestricted result. Execute `python3 checker.py` in a directory containing the extracted files.

## Relationship to prior work
An Abelian power is a sequence of adjacent blocks with identical Parikh vectors. Fici et al., *Abelian Repetitions in Sturmian Words* (2012; arXiv:1209.6013), and *Abelian Powers and Repetitions in Sturmian Words* (2015; arXiv:1506.02797) investigate Abelian repetition lengths and critical exponents primarily in Sturmian and Fibonacci words. Fici et al., *Algorithms for Computing Abelian Periods of Words* (2012; arXiv:1211.5389), supply general procedures for detecting Abelian periods. Their stated results concern different objects or algorithms and do not themselves imply the present all-length exact phase-count distribution on sparse binary necklaces. The OEIS entry A096168 counts Abelian-cube-free ternary linear words, not circular phase multiplicities with exactly three ones. The related broad literature motivates the question, but priority is not independently established.

## Limitations
The claim is restricted to exactly three ones, circumference divisible by three, and a three-block partition of the whole circle. It counts indexed cyclic cut positions, not necessarily distinct rotated strings; for the equally spaced three markers these quantities differ. It does not count shorter Abelian-cube *factors* or establish a phase law for an arbitrary marker count. The literature search and primary-text comparisons support a best-knowledge distinction, not proof of historical uniqueness or independent certification.

## References
1. G. Fici, A. Langiu, T. Lecroq, A. Lefebvre, F. Mignosi, É. Prieur-Gaston, *Abelian Repetitions in Sturmian Words*, arXiv:1209.6013, first public 2012-09-26, https://arxiv.org/abs/1209.6013.
2. G. Fici, T. Lecroq, A. Lefebvre, É. Prieur-Gaston, *Algorithms for Computing Abelian Periods of Words*, arXiv:1211.5389, first public 2012-11-22, https://arxiv.org/abs/1211.5389.
3. G. Fici et al., *Abelian Powers and Repetitions in Sturmian Words*, arXiv:1506.02797, first public 2015-06-09, https://arxiv.org/abs/1506.02797.
4. OEIS Foundation, A096168, *Number of Abelian cubefree words over a 3-letter alphabet*, https://oeis.org/A096168.
