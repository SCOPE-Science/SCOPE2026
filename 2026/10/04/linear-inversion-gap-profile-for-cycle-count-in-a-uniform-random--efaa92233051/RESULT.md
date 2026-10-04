# Linear inversion-gap profile for cycle count in a uniform random permutation

## Finding

Let \(\Pi\) be uniformly distributed on \(S_n\), with \(n\ge2\). Let
\[
C=C(\Pi)
\]
be the number of cycles of \(\Pi\), including fixed points. For
\[
1\le i<j\le n,
\]
define the ordinary one-line inversion indicator
\[
I_{ij}
=
\mathbf 1\{\Pi(i)>\Pi(j)\}.
\]

If
\[
d=j-i,
\]
then
\[
\boxed{
\operatorname{Cov}(C,I_{ij})
=
-\frac{2d-1}{2n(n-1)}.
}
\tag{1}
\]

Thus every inversion indicator is negatively covariant with cycle count, and the magnitude is an exact linear function of the positional gap.

Let
\[
V=\operatorname{inv}(\Pi)=\sum_{i<j}I_{ij}.
\]
Summing (1) gives
\[
\boxed{
\operatorname{Cov}(C,V)
=
-\frac{2n-1}{12}.
}
\tag{2}
\]

Write
\[
H_n=\sum_{k=1}^n\frac1k,
\qquad
H_n^{(2)}=\sum_{k=1}^n\frac1{k^2}.
\]
Using the classical variances of cycle count and inversion number,
\[
\operatorname{Var}(C)=H_n-H_n^{(2)}
\]
and
\[
\operatorname{Var}(V)
=
\frac{n(n-1)(2n+5)}{72},
\]
equation (2) yields
\[
\boxed{
\operatorname{Corr}(C,V)
=
-\frac{2n-1}
{\sqrt{2n(n-1)(2n+5)(H_n-H_n^{(2)})}}.
}
\tag{3}
\]
Consequently,
\[
\boxed{
\operatorname{Corr}(C,V)
\sim
-\frac1{\sqrt{n\log n}}.
}
\tag{4}
\]

There is also a direct Mallows interpretation. If \(\Pi_q\) has probability proportional to
\[
q^{\operatorname{inv}(\pi)},
\]
then
\[
\boxed{
\left.
\frac{d}{d\log q}
\mathbb E_q C(\Pi_q)
\right|_{q=1}
=
-\frac{2n-1}{12}.
}
\tag{5}
\]
Hence the uniform permutation has an exact finite-\(n\) cycle-count response to infinitesimal inversion tilting.

## Assumptions and scope

The inversions in (1) are the ordinary inversions of the one-line permutation:
\[
i<j,\qquad \Pi(i)>\Pi(j).
\]

This distinction matters because some permutation-pattern literature studies inversions after writing the permutation in a standardized cycle word. That is a different statistic.

The theorem concerns covariance and linear response at the uniform law. It does not claim that cycle count is monotone as a function of the inversion set of an individual permutation.

## Proof

Fix
\[
i<j
\]
and put
\[
s(\pi)
=
\begin{cases}
1,&\pi(i)>\pi(j),\\
-1,&\pi(i)<\pi(j).
\end{cases}
\]
Then
\[
s=2I_{ij}-1.
\]

Let \(T\pi\) be obtained by swapping the two images \(\pi(i)\) and \(\pi(j)\). Equivalently,
\[
T\pi=\pi\circ(i\,j).
\]
The map \(T\) is an involution preserving the uniform measure, and
\[
s(T\pi)=-s(\pi).
\]

Let
\[
S(\pi)
=
\mathbf 1\{i\text{ and }j\text{ belong to the same cycle of }\pi\}.
\]
Right multiplication by a transposition splits one cycle when the two transposed points lie in the same cycle, and merges two cycles otherwise. Therefore
\[
C(\pi)-C(T\pi)
=
1-2S(\pi).
\tag{6}
\]

Averaging a quantity with its image under \(T\),
\[
\mathbb E[Cs]
=
\frac12
\mathbb E\!\left[
s(\pi)\bigl(C(\pi)-C(T\pi)\bigr)
\right].
\]
Since
\[
\mathbb Es=0,
\]
equation (6) gives
\[
\mathbb E[Cs]
=
-\mathbb E[sS].
\tag{7}
\]
Also
\[
\operatorname{Cov}(C,I_{ij})
=
\frac12\mathbb E[Cs].
\tag{8}
\]

It remains to evaluate \(\mathbb E[sS]\).

Condition on the ordered pair
\[
\pi(i)=a,\qquad \pi(j)=b,
\qquad a\ne b.
\]
Each ordered distinct pair \((a,b)\) has probability
\[
\frac1{n(n-1)}.
\]

If
\[
a=i
\quad\text{or}\quad
b=j,
\]
then one of \(i,j\) is already a fixed point, so they cannot lie in the same cycle.

If
\[
a=j
\quad\text{or}\quad
b=i,
\]
there is already a directed path joining the two points, so they must lie in the same cycle.

In all remaining cases, the two specified arrows
\[
i\to a,\qquad j\to b
\]
are disjoint. Contracting each arrow produces a uniform permutation completion on \(n-2\) objects with two marked contracted objects. Two marked objects in a uniform permutation are in the same cycle with probability \(1/2\). Hence
\[
\Pr(S=1\mid \pi(i)=a,\pi(j)=b)
=
\begin{cases}
0,&a=i\text{ or }b=j,\\
1,&a=j\text{ or }b=i,\\
1/2,&\text{otherwise}.
\end{cases}
\tag{9}
\]

Now sum the sign
\[
\operatorname{sgn}(a-b)
\]
over these classes. The total sign over all ordered distinct pairs is zero. The sign sum over the probability-one class is
\[
2(j-i)-1,
\]
while the sign sum over the probability-zero class is
\[
-\bigl(2(j-i)-1\bigr).
\]
Using the baseline value \(1/2\) for all remaining pairs,
\[
\mathbb E[sS]
=
\frac{2(j-i)-1}{n(n-1)}.
\tag{10}
\]
Equations (7)--(10) prove (1).

Summing over all pairs,
\[
\operatorname{Cov}(C,V)
=
-\frac1{2n(n-1)}
\sum_{d=1}^{n-1}
(n-d)(2d-1).
\]
The elementary sum is
\[
\sum_{d=1}^{n-1}(n-d)(2d-1)
=
\frac{n(n-1)(2n-1)}6,
\]
which proves (2).

For completeness, the cycle-count variance follows from the standard Bernoulli-sum representation
\[
C\stackrel d=\sum_{k=1}^n B_k,
\qquad
B_k\sim\operatorname{Bernoulli}(1/k)
\]
independently. Thus
\[
\operatorname{Var}(C)=H_n-H_n^{(2)}.
\]
The Lehmer code gives
\[
V\stackrel d=\sum_{k=1}^n U_k,
\]
where the \(U_k\) are independent and uniform on
\[
\{0,\ldots,k-1\}.
\]
Therefore
\[
\operatorname{Var}(V)
=
\sum_{k=1}^n\frac{k^2-1}{12}
=
\frac{n(n-1)(2n+5)}{72}.
\]
This proves (3), and (4) follows from
\[
H_n-H_n^{(2)}\sim\log n.
\]

Finally, for the Mallows law,
\[
\mathbb P_q(\pi)
=
\frac{q^{V(\pi)}}{Z_n(q)}.
\]
Differentiation with respect to
\[
\theta=\log q
\]
gives the standard exponential-family identity
\[
\frac{d}{d\theta}\mathbb E_\theta C
=
\operatorname{Cov}_\theta(C,V).
\]
Evaluating at \(q=1\) and using (2) proves (5).

## Verification

The accompanying checker exhaustively enumerates all permutations through \(n=8\).

For every pair \(i<j\), it reconstructs the exact covariance between cycle count and the corresponding ordinary inversion indicator and verifies the gap law (1).

It also verifies the conditional same-cycle rule (9), the total covariance (2), the exact cycle-count and inversion variances, and the squared correlation formula.

The finite replay is supplementary. The all-\(n\) theorem is proved by the image-swap involution and the exact completion count above.

## Relationship to prior work

Gladkich and Peled study cycle structure under the Mallows law, where a permutation receives weight proportional to \(q^{\operatorname{inv}(\pi)}\). Their paper specifically analyzes the expected number of cycles and shows its order across the Mallows parameter range. The uniform law is the point \(q=1\). Their theorem does not state the exact derivative at \(q=1\), the covariance with inversion number, or the gap-resolved contribution of each inversion indicator.

He, Müller, and Verstraaten later study cycle counts in Mallows permutations in substantially greater asymptotic detail. Their full text likewise formulates the model using ordinary inversion number and cycle counts, but does not state a covariance between total cycle count and inversion number.

Parviainen gives a joint generating function involving cycles and “inversions,” but the paper explicitly defines those inversions as occurrences after writing the permutation in standard cycle form. This is not the ordinary one-line inversion statistic used by the Mallows law and in the present theorem. The difference is material: the local covariance profile (1) depends on the original positions \(i,j\).

Targeted searches for cycle-count/inversion covariance, Mallows derivatives at \(q=1\), and gap-resolved inversion contributions did not locate (1)--(5).

## Limitations

The result is a uniform-point covariance and first-order Mallows response. It does not determine the full expected-cycle function for \(q\ne1\).

The local formula is specific to ordinary one-line inversions. Other Mahonian or cycle-word inversion statistics can have different joint laws with cycle count.

The proof is elementary once the image-swap involution and the completion rule (9) are recognized. Older enumerative permutation literature may therefore contain an equivalent mixed first moment under different notation; this remains the principal originality risk.

## References

1. A. Gladkich and R. Peled, “On the Cycle Structure of Mallows Permutations,” arXiv:1601.06991, first submitted 2016-01-26; later *The Annals of Probability* 46 (2018), 1114–1169, DOI 10.1214/17-AOP1202.
2. J. He, T. Müller, and T. W. Verstraaten, “Cycles in Mallows random permutations,” arXiv:2201.11610; *Random Structures & Algorithms* 63 (2023), 1054–1099.
3. R. Parviainen, “Cycles and patterns in permutations,” arXiv:math/0610616, first submitted 2006-10-20.
