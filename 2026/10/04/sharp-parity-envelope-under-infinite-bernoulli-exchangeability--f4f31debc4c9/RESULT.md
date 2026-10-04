# Sharp parity envelope under infinite Bernoulli exchangeability

## Finding

Let \((X_i)_{i\ge1}\) be an infinitely exchangeable Bernoulli sequence with
\[
\Pr(X_i=1)=\mu,
\]
and for an integer \(n\ge2\) put
\[
K_n=\sum_{i=1}^n X_i,
\qquad
m=1-2\mu.
\]

If \(n\) is even, the exact attainable interval is
\[
\boxed{
\frac{1+m^n}{2}
\le
\Pr(K_n\ {\rm even})
\le
1.
}
\]

If \(n\ge3\) is odd, let \(c_n\in(0,1)\) be the unique solution of
\[
c_n^{\,n-1}\bigl[n+(n-1)c_n\bigr]=1.
\]
Define
\[
U_n(m)=
\begin{cases}
m^n,&-1\le m\le-c_n,\\[1mm]
n c_n^{\,n-1}m+(n-1)c_n^n,&-c_n\le m\le1,
\end{cases}
\]
and
\[
L_n(m)=-U_n(-m).
\]
Then the exact attainable interval is
\[
\boxed{
\frac{1+L_n(m)}2
\le
\Pr(K_n\ {\rm even})
\le
\frac{1+U_n(m)}2.
}
\]

Every value between the two endpoints is attainable. Each endpoint can be
realized by a de Finetti mixing law having at most two atoms.

For the fair marginal \(\mu=1/2\), even and odd sample sizes have sharply
different behavior. Every even \(n\) has
\[
\Pr(K_n\ {\rm even})\in[1/2,1],
\]
whereas for odd \(n\),
\[
\Pr(K_n\ {\rm even})
\in
\left[
\frac{1-(n-1)c_n^n}{2},
\frac{1+(n-1)c_n^n}{2}
\right],
\]
and this interval converges to
\[
[1/4,3/4].
\]

## Assumptions and scope

The sequence is infinitely exchangeable, not merely exchangeable at a fixed
finite length. The distinction is essential: infinite exchangeability invokes
the de Finetti mixture representation and therefore restricts the law of
\(K_n\) to mixtures of binomial laws.

Only the one-dimensional marginal \(\mu\) is prescribed. No pair correlation,
higher moment, or parametric form of the de Finetti mixing law is assumed.

The theorem concerns parity. It does not claim the analogous closed form for
other residue classes modulo an integer larger than \(2\).

## Proof

By de Finetti's representation theorem there is a random variable
\(P\in[0,1]\) such that, conditionally on \(P\), the variables \(X_i\) are
independent Bernoulli variables with parameter \(P\). The fixed marginal gives
\[
\mathbb E P=\mu.
\]
Set
\[
M=1-2P.
\]
Then \(M\in[-1,1]\) and
\[
\mathbb E M=m.
\]

Conditionally on \(P\),
\[
\mathbb E\!\left[(-1)^{K_n}\mid P\right]
=
(1-2P)^n.
\]
Hence the parity bias is
\[
2\Pr(K_n\ {\rm even})-1
=
\mathbb E M^n.
\tag{1}
\]
The problem is therefore the exact range of the \(n\)-th moment of a random
variable on \([-1,1]\) with prescribed mean \(m\).

For even \(n\), the function
\[
f(x)=x^n
\]
is convex on \([-1,1]\). Jensen's inequality gives
\[
\mathbb E M^n\ge m^n.
\]
Equality is attained by \(M=m\) almost surely, corresponding to the iid
Bernoulli sequence with parameter \(\mu\). Since \(M^n\le1\),
\[
\mathbb E M^n\le1.
\]
The upper endpoint is attained by the two-point law on \(\{-1,1\}\) having
mean \(m\). This proves the even case.

Now let \(n\ge3\) be odd. The function
\[
h(c)=c^{\,n-1}\bigl[n+(n-1)c\bigr]
\]
is strictly increasing on \((0,1)\), with \(h(0)=0\) and \(h(1)=2n-1\).
Thus there is a unique \(c_n\in(0,1)\) satisfying \(h(c_n)=1\).

Write \(c=c_n\). The line tangent to \(x^n\) at \(x=-c\) is
\[
\ell(x)=n c^{\,n-1}x+(n-1)c^n.
\]
The defining equation for \(c\) says exactly that
\[
\ell(1)=1.
\]
Moreover
\[
g(x):=\ell(x)-x^n
\]
satisfies
\[
g(-c)=g(1)=0
\]
and
\[
g'(x)=n\bigl(c^{\,n-1}-x^{\,n-1}\bigr).
\]
Because \(n-1\) is even, \(g\) increases on \([-c,c]\) and decreases on
\([c,1]\). Therefore
\[
\ell(x)\ge x^n
\qquad(-c\le x\le1).
\]

On \([-1,-c]\), the function \(x^n\) is concave. Its derivative matches the
slope of \(\ell\) at \(-c\). Consequently
\[
U_n(x)=
\begin{cases}
x^n,&-1\le x\le-c,\\
\ell(x),&-c\le x\le1
\end{cases}
\]
is concave and majorizes \(x^n\).

It is the least concave majorant. Indeed, any concave majorant must dominate
\(x^n\) on \([-1,-c]\). On \([-c,1]\), concavity forces it above the chord
joining \((-c,-c^n)\) to \((1,1)\), and that chord is precisely \(\ell\).
Thus
\[
\mathbb E M^n\le U_n(m).
\tag{2}
\]

The endpoint in (2) is explicit. If \(m\le-c\), take \(M=m\) almost surely.
If \(m\ge-c\), take
\[
M\in\{-c,1\}
\]
with
\[
\Pr(M=1)=\frac{m+c}{1+c},
\qquad
\Pr(M=-c)=\frac{1-m}{1+c}.
\]
This law has mean \(m\), and its \(n\)-th moment is the chord value \(U_n(m)\).

Because \(x^n\) is odd, the greatest convex minorant is
\[
L_n(m)=-U_n(-m).
\]
Equivalently, if \(m\ge c\), the lower endpoint is attained by the degenerate
law \(M=m\); if \(m\le c\), it is attained by a two-point law on
\[
\{-1,c\}.
\]
Hence
\[
L_n(m)\le\mathbb E M^n\le U_n(m),
\]
with both endpoints attained.

Convex mixtures of two mixing laws having the same mean \(m\) preserve that
mean and interpolate their \(n\)-th moments. Thus every value between the
endpoints is attainable. Equation (1) converts the moment interval to the
stated parity-probability interval.

For the fair marginal, \(m=0\), so the odd-\(n\) parity bias ranges over
\[
[-(n-1)c_n^n,\,(n-1)c_n^n].
\]
The defining equation yields
\[
(n-1)c_n^n
=
\frac{(n-1)c_n}{n+(n-1)c_n}.
\tag{3}
\]
Also \(c_n\to1\): otherwise a subsequence bounded away from \(1\) would make
the left side of the defining equation tend to \(0\), contradicting its value
\(1\). Taking the limit in (3) gives
\[
(n-1)c_n^n\longrightarrow\frac12.
\]
This proves the limiting fair-marginal interval \([1/4,3/4]\).

## Verification

The accompanying checker solves the defining equation for \(c_n\) by
high-precision bisection for odd \(n\), verifies the tangent equation, and
checks the upper and lower envelope inequalities on a dense grid. It also
constructs the one- and two-atom extremal mixing laws and checks their means
and parity moments numerically at high precision.

The checker separately verifies the exact special case \(n=3\), where
\[
c_3=\frac12,
\]
and confirms the fair-marginal asymptotic trend through large odd sample sizes.

These computations replay the formulas. The universal proof is the
concave/convex-envelope argument above.

## Relationship to prior work

Rougier gives a self-contained finite representation theorem for exchangeable
sequences and emphasizes the distinction between finite exchangeability and
arbitrary extendibility. In the extendible limit, the relevant representation
becomes the classical de Finetti mixture of iid laws. This supplies the
representation-theoretic starting point used here.

Zaigraev and Kaniovski derive exact upper and lower probabilities of monotone
tail events for finite exchangeable Bernoulli trials with a prescribed
marginal, using linear programming. Their event is the probability of at
least a fixed number of successes; they do not impose infinite extendibility
and do not treat the alternating parity event.

A closely related published result on infinitely extendible Bernoulli
sequences gives exact envelopes for tail probabilities by taking concave and
convex envelopes of binomial-tail functions under the de Finetti mean
constraint. That framework explains why one-dimensional envelope geometry is
natural here. The parity objective is different: its conditional expectation
is the pure power \((1-2P)^n\), producing the even/odd phase split, the
odd-power tangent equation for \(c_n\), explicit two-atom parity extremizers,
and the fair-marginal limit \([1/4,3/4]\). None of those parity statements is
contained in the closest tail result.

Targeted searches using parity, XOR, binomial-mixture, de Finetti, and
exchangeable-Bernoulli terminology did not locate an equivalent parity
envelope.

## Limitations

The result uses infinite exchangeability. A finite exchangeable Bernoulli
vector can have a wider feasible parity range because not every finite
exchangeable law is infinitely extendible.

The closed form is specific to parity. For residues modulo integers larger
than \(2\), the conditional residue probabilities are trigonometric
polynomials rather than one real power, so their envelope geometry can have
more pieces.

The originality assessment is based on targeted statement-level searches and
inspection of the closest full texts. An equivalent parity formula could
exist in older exchangeability or moment-problem literature under terminology
not captured by those searches.

## References

1. J. Rougier, “Exchangeability, the ‘Histogram Theorem’, and population
   inference,” arXiv:1511.03551, first submitted 2015-11-11.
2. A. Zaigraev and S. Kaniovski, “Exact bounds on the probability of at least
   \(k\) successes in \(n\) exchangeable Bernoulli trials as a function of
   correlation coefficients,” preprint dated 2010-03-28.
3. P. Diaconis and D. Freedman, “Finite exchangeable sequences,”
   *The Annals of Probability* 8 (1980), 745–764.
4. D. Heath and W. Sudderth, “De Finetti’s theorem on exchangeable
   variables,” *The American Statistician* 30 (1976), 188–189.
