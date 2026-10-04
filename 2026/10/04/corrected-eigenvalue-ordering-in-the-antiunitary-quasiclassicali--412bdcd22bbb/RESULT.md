# Corrected eigenvalue ordering in the antiunitary quasiclassicality roof

## Finding

Oszmaniec and Kuś give, in their Eq. (19), an antiunitary convex-roof formula of the form
\[
f_1^\cup(\rho)
=
\max\!\left\{0,\mu_1-\sum_{j=2}^r\mu_j}\right\}.
\]
Immediately after the display they describe the \(\mu_j\) as the increasingly ordered eigenvalues of
\[
\left|\sqrt\rho\,\widetilde\theta\,\sqrt\rho\right|.
\]
That ordering descriptor is reversed. The formula is correct only when the values are labeled in nonincreasing order,
\[
\boxed{\mu_1\ge\mu_2\ge\cdots\ge\mu_r\ge0}.
\]
Equivalently, \(\mu_1\) must denote the largest eigenvalue.

The distinction is mathematically operative. Under the literal nondecreasing interpretation,
\[
\mu_1\le\mu_2\le\cdots\le\mu_r,
\]
and for every \(r\ge2\),
\[
\mu_1-\sum_{j=2}^r\mu_j
\le
\mu_1-\mu_2
\le0.
\]
Thus the printed ordering would force Eq. (19) to return zero in every instance with at least two listed eigenvalues, nullifying the mixed-state detection role of the formula.

A concrete two-qubit witness is the Bell-white-noise family
\[
\rho_p
=
p|\Phi^+\rangle\langle\Phi^+|
+
\frac{1-p}4 I,
\qquad
|\Phi^+\rangle
=
\frac{|00\rangle+|11\rangle}{\sqrt2}.
\]
For the usual spin-flip antiunitary, \(\rho_p\) is spin-flip invariant. The eigenvalues entering the roof are therefore
\[
b=\frac{1+3p}4,
\qquad
a=\frac{1-p}4
\]
with \(a\) repeated three times. Descending order yields
\[
\boxed{
f_1^\cup(\rho_p)
=
\max\!\left\{0,b-3a}\right\}
=
\max\!\left\{0,\frac{3p-1}2}\right\}.
}
\]
At \(p=1/2\), this equals \(1/4\). Reading the source's ordering descriptor literally instead puts an \(a\) in the first position and gives zero.

## Assumptions and scope

The statement concerns Eq. (19) of the cited paper and the ordering convention for the nonnegative eigenvalues of the positive operator
\[
\left|\sqrt\rho\,\widetilde\theta\,\sqrt\rho\right|.
\]
The correction does not alter the displayed algebraic form of Eq. (19); it changes only which eigenvalue is called \(\mu_1\).

The two-qubit example uses the standard spin-flip antiunitary and the usual Bell state \(|\Phi^+\rangle\). The witness is included to show that the ordering issue changes the value of the mixed-state detector, not merely notation.

No claim is made that the antiunitary roof formula itself is new. It is the earlier result of Uhlmann that the paper cites.

## Proof

Uhlmann's Proposition 4.1 states the relevant roof formula with the eigenvalues ordered
\[
\lambda_1\ge\lambda_2\ge\cdots\ge0
\]
and gives
\[
g^\cup(\omega)
=
\max\!\left\{0,\lambda_1-\sum_{j>1}\lambda_j}\right\}.
\]
Oszmaniec and Kuś reproduce the same largest-minus-the-rest expression in Eq. (19) but describe the eigenvalues as increasingly ordered. The two conventions are incompatible unless the word describing the ordering is reversed or \(\mu_1\) is explicitly redefined as the largest value.

The collapse under literal increasing order is immediate: for \(r\ge2\), all eigenvalues are nonnegative and \(\mu_2\ge\mu_1\), so
\[
\mu_1-\sum_{j=2}^r\mu_j
\le
\mu_1-\mu_2
\le0.
\]
Taking the maximum with zero then gives zero.

For the Bell-white-noise witness, the Bell projector and identity are both invariant under the spin flip. Hence the antiunitary roof spectrum coincides with the ordinary spectrum of \(\rho_p\): one eigenvalue
\[
b=\frac{1+3p}4
\]
and three eigenvalues
\[
a=\frac{1-p}4.
\]
Because \(b\ge a\) for \(p\in[0,1]\), descending order gives
\[
b-3a
=
\frac{1+3p-3+3p}4
=
\frac{3p-1}2.
\]
This proves the stated corrected value. At \(p=1/2\), it is \(1/4\), while literal ascending order gives a nonpositive first-minus-rest expression and therefore zero.

## Verification

`verify_ordering_correction.py` checks the ordering-collapse inequality on exhaustive rational test grids, verifies the Bell-white-noise spectrum algebra exactly with rational arithmetic, and confirms the \(p=1/2\) discrepancy.

The decisive correctness check is textual and theorem-level rather than numerical: the source's Eq. (19) is paired with the phrase “increasingly ordered,” whereas Uhlmann's cited proposition explicitly uses \(\lambda_1\ge\lambda_2\ge\cdots\). The elementary inequality above then proves the consequence of the literal reading.

## Relationship to prior work

The corrected formula is not a new convex-roof theorem. Uhlmann's 2010 Proposition 4.1 already gives the general antiunitary roof in descending eigenvalue order. Oszmaniec and Kuś cite that result and apply it to their quasiclassicality framework.

The finding here is narrower: the ordering word accompanying Eq. (19) in the later paper is reversed, and reading it literally destroys the mixed-state detector. Targeted searches for the paper title together with ordering, Eq. (19), erratum, correction, and decreasing-order terminology did not locate an indexed correction. The same increasing-order wording is present in the arXiv manuscript and in an author-uploaded journal-text copy inspected during comparison.

The two-qubit Bell-white-noise calculation is an explicit impact witness, not a claim of a new concurrence formula.

## Limitations

The correction is confined to the ordering descriptor attached to Eq. (19). It does not reassess the paper's representation-theoretic classification results, its pure-state criteria, or later applications.

An informal correction may exist outside the indexed literature searched. The mathematical need for descending order, however, follows independently from Uhlmann's cited proposition and from the collapse of the literal ascending interpretation.

## References

1. M. Oszmaniec and M. Kuś, “On detection of quasiclassical states,” arXiv:1111.1005, first submitted 3 November 2011; *Journal of Physics A: Mathematical and Theoretical* 45 (2012), 244034, DOI: 10.1088/1751-8113/45/24/244034.
2. A. Uhlmann, “Roofs and Convexity,” *Entropy* 12 (2010), 1799–1832, DOI: 10.3390/e12071799.
