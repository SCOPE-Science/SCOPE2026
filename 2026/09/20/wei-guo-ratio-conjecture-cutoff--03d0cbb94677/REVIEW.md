# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The argument was checked independently at the algebraic, zero-location, and
analytic-continuation steps.

For \(q=e^{-t}\), the standard identity
\[
\operatorname{Li}_{-n}(q)
=\sum_{m\ge1}m^nq^m
=\frac{qA_n(q)}{(1-q)^{n+1}}
\]
gives
\[
\mathcal F_i(t)
=\frac{A_{i+1}(q)}{(1-q)A_i(q)}.
\]
The indexing was checked explicitly through
\[
A_1=1,\quad A_2=1+q,\quad A_3=1+4q+q^2,\quad
A_4=1+11q+11q^2+q^3.
\]

The recurrence
\[
A_{n+1}=q(1-q)A_n'+(1+nq)A_n
\]
proves by induction that \(A_n\) is monic with constant term \(1\) and has
simple negative roots. At a root \(r\) of \(A_n\),
\[
A_{n+1}(r)=r(1-r)A_n'(r),
\]
so consecutive Eulerian polynomials have no common root. The sign changes at
successive roots, together with the signs at \(0\) and at \(-\infty\), give
the full interlacing induction.

For \(n\ge3\), the absolute product of the roots is \(1\). If all root
moduli were at least \(1\), all would have modulus exactly \(1\), forcing
all negative roots to equal \(-1\), contrary to simplicity. Thus there is a
root \(r\in(-1,0)\).

For \(i\ge3\), that root yields
\[
z_0=-\log(-r)-i\pi,\qquad \Re z_0>0,\qquad e^{-z_0}=r.
\]
The denominator of
\[
\frac{A_{i+1}(e^{-z})}{(1-e^{-z})A_i(e^{-z})}
\]
vanishes at \(z_0\), whereas the numerator does not, so the singularity is a
genuine pole.

The analytic obstruction was also checked. A completely monotone function
is a Laplace transform of a nonnegative measure. Its Laplace integral is
holomorphic on \(\Re z>0\); local differentiation is justified by comparing
\(s^k e^{-\sigma s}\) with a constant multiple of
\(e^{-\sigma s/2}\). Identity on the positive real axis would force this
holomorphic extension to equal the meromorphic Eulerian quotient away from
its poles. A genuine pole inside the half-plane is therefore impossible.

The positive cases are explicit positive discrete Laplace transforms:
\[
\mathcal F_0=\frac1{1-q},\qquad
\mathcal G_0=\frac q{1-q},
\]
\[
\mathcal F_1=\mathcal G_1
=1+2\sum_{m\ge1}q^m,
\]
and
\[
\mathcal F_2=\mathcal G_2
=1+4\sum_{m\ge0}q^{2m+1}+2\sum_{m\ge1}q^{2m}.
\]
Hence there is no missing boundary case.

## Originality

Wei and Guo's 2014 paper explicitly states Conjecture 12 that all
\(\mathcal F_i\) and \(\mathcal G_i\) should be completely monotone. Its full
text was inspected, including the ratio theorem, the polylogarithm
reformulation, and the conjecture section.

Searches covered the exact title and DOI, "Conjecture 12", the consecutive
negative-order polylogarithm ratio, Eulerian-polynomial quotient
formulations, and combinations with complete monotonicity, Laplace
transforms, analytic continuation, poles, and Eulerian zeros. Citation and
later-literature searches through the publication date did not locate a
resolution. Later work on Eulerian real-rootedness confirms the classical
zero structure but does not address the Wei–Guo ratio conjecture.

No specific inaccessible paper was identified as likely to contain a prior
resolution. The residual originality risk is a result stated under
substantially different terminology, or an unpublished or poorly indexed
observation. The originality assessment is therefore "to the best of our
knowledge", not an exhaustive-literature guarantee.

## Value

The result completely settles a named 2014 conjecture rather than giving an
isolated counterexample. It identifies the exact positive range
\(i=0,1,2\), proves failure for every \(i\ge3\), and gives a reusable
structural obstruction: real zeros of an Eulerian denominator become
right-half-plane poles after the exponential substitution, while complete
monotonicity would force right-half-plane holomorphy.

The first failure is already explicit:
\(A_3(q)=q^2+4q+1\) gives the pole
\[
\log(2+\sqrt3)-i\pi.
\]

## Limitations

The proof does not identify the first derivative order at which complete
monotonicity fails for each \(i\ge3\), nor the first real \(t>0\) witnessing
a sign violation. It does not classify stronger notions such as logarithmic
complete monotonicity. A differently phrased, unpublished, or poorly indexed
prior resolution may exist. Independent audit has not been performed.
