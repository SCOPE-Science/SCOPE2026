# Covering radius three for two extended two-weight BCH families
## Finding
Let \(\overline{\mathcal C}^A_s\) be the parity extension of the binary BCH code \(\mathcal C_{(2,n_A,3,1)}\) with
\[
n_A=(2^{2s}+1)(2^s-1),\qquad s\ge2,
\]
and let \(\overline{\mathcal C}^B_s\) be the parity extension of the binary BCH code \(\mathcal C_{(2,n_B,3,1)}\) with
\[
n_B=\frac{2^{2s}-1}{3},\qquad s\ge4.
\]
Then
\[
\rho(\overline{\mathcal C}^A_s)=\rho(\overline{\mathcal C}^B_s)=3.
\]
More precisely, for either family write \(r\) for the redundancy of the unextended code and \(N=n+1\) for the extension length. Thus \(r=4s\) in Family A and \(r=2s\) in Family B. The \(2^{r+1}\) cosets of the extended code have leader-weight distribution
\[
L_0=1,\qquad L_1=N,\qquad L_2=2^r-1,\qquad L_3=2^r-N.
\]
In particular, every coset has a leader of weight at most three and at least one coset has no leader of weight at most two.

## Assumptions and scope
The covering radius \(\rho(C)\) is the largest minimum Hamming distance from a binary word to the code \(C\). A parity extension appends the overall parity coordinate, so the extended code is even. A coset leader is a minimum-weight vector in a coset; \(L_j\) counts cosets whose leader weight is \(j\).

The source paper proves for Family A that the unextended code has parameters \([n_A,n_A-4s,3]\) and that its dual has exactly two nonzero weights (Theorem 4.2), while the parity extension has parameters \([n_A+1,n_A-4s,4]\) (Theorem 4.5). For Family B it proves the analogous statements \([n_B,n_B-2s,3]\) with a two-nonzero-weight dual (Theorem 6.2) and \([n_B+1,n_B-2s,4]\) for the parity extension (Theorem 6.5), for \(s\ge4\).

## Proof
We first use a general lemma. Let \(C\) be a binary \([n,n-r,3]\) linear code whose dual has exactly two nonzero weights, and suppose \(n+1<2^r\). Let \(\overline C\) be its parity extension and suppose \(d(\overline C)=4\).

The external distance of \(C\) is the number of nonzero weights of \(C^\perp\), hence it is two. Delsarte's external-distance bound gives
\[
\rho(C)\le2.
\]
The radius cannot be one. Because \(d(C)=3\), radius-one balls around codewords are disjoint; if they covered the whole space then the Hamming perfect-code identity would force
\[
(n+1)2^{n-r}=2^n,
\]
that is \(n+1=2^r\), contrary to the hypothesis. Therefore \(\rho(C)=2\).

Choose a full-rank parity-check matrix \(H\) of \(C\). A parity-check matrix of the parity extension is row-equivalent to
\[
\overline H=
\begin{pmatrix}
H&0\\
1&\cdots&1&1
\end{pmatrix}.
\]
The last syndrome coordinate is therefore the parity of the error weight.

Consider first the \(2^r\) syndromes with last coordinate zero. The zero syndrome has leader weight zero. Every nonzero \(r\)-bit base syndrome has a representation by one or two columns of \(H\), because \(\rho(C)=2\). If it is one column \(h_i\), then \((h_i,0)\) is the sum of the extended column \((h_i,1)\) and the new parity-coordinate column \((0,1)\). If it is \(h_i+h_j\), then \((h_i+h_j,0)\) is the sum of the two corresponding extended columns. Hence every nonzero last-zero syndrome has extended leader weight exactly two. Thus
\[
L_0=1,\qquad L_2=2^r-1.
\]

Now consider syndromes with last coordinate one. The \(N=n+1\) columns of \(\overline H\) are distinct because \(d(\overline C)=4\), so exactly \(N\) such syndromes have leader weight one. Any remaining last-one syndrome cannot have leader weight zero, one, or two: weights zero and two have even parity syndrome, and the weight-one syndromes are precisely the columns just counted. On the other hand, if its first \(r\) coordinates are \(y\), then \(y\) is not zero and is not a column of \(H\); since \(\rho(C)=2\), it equals \(h_i+h_j\) for distinct coordinates \(i,j\). Adding the new parity coordinate gives a three-column representation of \((y,1)\). Hence every remaining last-one syndrome has leader weight exactly three, giving
\[
L_1=N,\qquad L_3=2^r-N.
\]
The assumed inequality \(N<2^r\) makes \(L_3>0\), so \(\rho(\overline C)=3\).

For Family A,
\[
N_A=2^{3s}-2^{2s}+2^s<2^{4s}=2^{r_A},
\]
and the source theorem supplies the two-weight dual and extended distance four. For Family B,
\[
N_B=\frac{2^{2s}+2}{3}<2^{2s}=2^{r_B},
\]
and the corresponding source theorems supply the same hypotheses. The lemma therefore proves the stated radii and the complete coset-leader distributions.

## Verification
Run `python verify.py`. The script checks the parameter identities and leader-count formulas over representative ranges of \(s\), and independently reconstructs the syndrome graphs for the smallest convenient anchors: Family A at \(s=2\), giving \((L_0,L_1,L_2,L_3)=(1,52,255,204)\), and Family B at \(s=4\), giving \((1,86,255,170)\). Both finite checks use \(\mathbb F_{256}\) and exact breadth-first search on all \(512\) syndromes.

These finite computations are sanity checks only. The infinite-family statement is proved by the external-distance argument above, not by extrapolation from finite cases.

## Relationship to prior work
Chen, Xie, and Ding explicitly ask in Open Problem 8.6 for the covering radii of the distance-optimal binary codes presented in their paper. Their Theorems 4.2 and 6.2 provide the two-weight dual distributions of the two punctured families used here, and Theorems 4.5 and 6.5 construct the corresponding distance-four parity extensions, but the paper does not state the covering radii or the coset-leader distributions above.

The Delsarte external-distance inequality \(\rho(C)\le s(C)\), where \(s(C)\) is the number of nonzero dual weights, is standard and is restated as Lemma 8(i) in the cited covering-radius literature. Earlier work on covering radii of binary cyclic codes computes other families and parameter ranges, but the inspected tables and statements do not contain these two extended BCH families. Focused searches using the source notation, both length formulas, the exact redundancies, and the phrase “covering radius three” did not locate a prior statement of the present result.

## Limitations
The claim settles the covering radius only for the two distance-four families whose punctured codes have exactly two nonzero dual weights. It does not determine the radius of the other distance-optimal families in the source paper, including its distance-six constructions or the Section 5 distance-four family. The proof depends on the published two-weight enumerators and the standard Delsarte external-distance bound. The packaged finite checks do not constitute an independent proof of the infinite theorem. Focused database and literature searches reduce but cannot eliminate the possibility of an older unindexed equivalent statement.

## References
H. Chen, C. Xie, and C. Ding, *Infinitely many families of distance-optimal binary linear codes with respect to the sphere packing bound*, arXiv:2510.22259v1, 25 October 2025. See Theorems 4.2, 4.5, 6.2, 6.5, and Open Problem 8.6.

*On self-dual completely regular codes with covering radius \(\rho\le3\)*, Finite Fields and Their Applications, 2025, DOI:10.1016/j.ffa.2025.102617. Lemma 8(i) restates Delsarte's external-distance bound \(\rho\le s\).

M. Arce-Nazario, R. Castro, and J. Ortiz-Ubarri, *On the covering radius of some binary cyclic codes*, Advances in Mathematics of Communications 11 (2017), DOI:10.3934/amc.2017025.
