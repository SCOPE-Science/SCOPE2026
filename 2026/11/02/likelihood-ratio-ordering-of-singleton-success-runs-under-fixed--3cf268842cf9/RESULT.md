# Likelihood-ratio ordering of singleton success runs under fixed composition

## Finding

Let a binary word be drawn uniformly among all words with exactly \(a\) ones and \(b\) zeros, where \(a\ge2\) and \(b\ge1\). Let \(R\) be the number of maximal runs of ones and \(S\) the number of these runs having length exactly one. For every pair \(1\le r_1<r_2\le\min(a,b+1)\), and every \(0\le s_1<s_2\le a\), the conditional joint kernel satisfies

\[
\Pr(S=s_1\mid R=r_1)\Pr(S=s_2\mid R=r_2)
\ge
\Pr(S=s_2\mid R=r_1)\Pr(S=s_1\mid R=r_2).
\]

Equivalently, the family of singleton-run laws is increasing in likelihood-ratio order as the number of one-runs increases. The joint law of \((R,S)\) is totally positive of order two. The conditional laws depend on \(a\) and \(r\), but not on the number \(b\) of zeros, once that run count is feasible. They obey the exact formula

\[
\Pr(S=s\mid R=r)=
\frac{\binom r s\binom{a-r-1}{r-s-1}}{\binom{a-1}{r-1}}
\quad\text{if }r<a,
\]

where out-of-range binomial coefficients are zero; for \(r=a\), \(S=a\) with probability one. In particular, for every such nondegenerate composition,

\[
\operatorname{Cov}(R,S)=
\frac{2ab^2(a-1)(b+1)}{(a+b)^2(a+b-1)(a+b-2)}>0.
\]

## Assumptions and scope

A run of ones is a maximal nonempty contiguous block of ones, including at either end of the word. The sample space consists of the \(\binom{a+b}{a}\) equiprobable words with prescribed counts \(a\) and \(b\); it is not an independent Bernoulli sample conditioned only on a run count. A feasible run count has \(1\le r\le\min(a,b+1)\). All probabilities are exact finite-sample probabilities. The likelihood-ratio statement uses the nonnegative-minor definition, so support zeros create no division ambiguities. For \(a=1\) or \(b=0\), the two statistics are deterministic; these degenerate cases are excluded from the strict covariance claim.

## Proof

**1. Uniform compositions under run conditioning.** Every word with \(R=r\) has an ordered positive composition \((L_1,\ldots,L_r)\) of \(a\), consisting of its successive one-run lengths. Once those lengths are fixed, the \(b\) zeros must fill \(r+1\) gaps, with at least one zero in each of the \(r-1\) interior gaps. The number of placements is \(\binom{b+1}{r}\), independent of the composition. Thus, conditional on \(R=r\), the vector of run lengths is uniform over the \(\binom{a-1}{r-1}\) positive compositions of \(a\) into \(r\) parts.

When \(r<a\), to obtain exactly \(s\) singleton parts choose their positions in \(\binom r s\) ways. The other \(r-s\) parts are at least two, and distributing the remaining \(a-s-2(r-s)=a-2r+s\) units among them gives \(\binom{a-r-1}{r-s-1}\) choices. All of these quantities are nonnegative precisely when \(\max(0,2r-a)\le s\le r-1\). This proves the conditional mass formula. When \(r=a\), all parts equal one.

**2. Exact likelihood-ratio comparison.** Put \(N_r(s)=\binom r s\binom{a-r-1}{r-s-1}\) for \(r<a\), with zero entries outside the feasible support. Each support is an integer interval \([\max(0,2r-a),r-1]\). Both endpoints shift weakly to the right when \(r\) increases; the final row \(r=a\) has singleton support \(\{a\}\).

For adjacent rows \(r,r+1\), whenever both entries at \(s\) are positive, write \(d=a-r\) and \(u=r-s\). Direct cancellation gives

\[
\frac{N_{r+1}(s)}{N_r(s)}
=\frac{(r+1)(d-u)(d-u-1)}{(u+1)u(d-1)}.
\]

On their common support, \(u\ge1\), \(d-u\ge2\), and \(d\ge2\). As \(s\) increases, \(u\) decreases, so each numerator factor weakly increases and each denominator factor weakly decreases, with a strict change between distinct common-support arguments. Thus the ratio increases strictly wherever two such arguments exist. The moving support endpoints show that the cross-product inequalities also hold for entries lying outside the overlap. The last transition to the point mass at \(s=a\) is ordered by disjoint supports. This proves likelihood-ratio order for adjacent feasible rows; transitivity yields all \(r_1<r_2\). Multiplication of a row by \(\Pr(R=r)>0\) preserves every two-by-two minor, proving total positivity of order two for the joint mass matrix.

**3. Exact covariance.** The word-count formula from step 1 gives

\[
\Pr(R=r)=\frac{\binom{a-1}{r-1}\binom{b+1}{r}}{\binom{a+b}{a}}.
\]

Marking a singleton position in a uniform positive composition yields \(\mathbb E[S\mid R=r]=r(r-1)/(a-1)\), including \(r=a\). Write \(n=a+b\). For each \(t=1,2,3\), the Vandermonde identity and \(\binom r t\binom{b+1}{r}=\binom{b+1}{t}\binom{b+1-t}{r-t}\) imply

\[
\mathbb E[(R)_t]
=\frac{(a)_t(b+1)_t}{(n)_t},
\]

where \((z)_t=z(z-1)\cdots(z-t+1)\). Since \(R(R)_2=(R)_3+2(R)_2\),

\[
\operatorname{Cov}(R,S)
=\frac{\mathbb E[(R)_3]+(2-\mathbb ER)\mathbb E[(R)_2]}{a-1}.
\]

Substituting the three factorial moments and cancelling produces the stated rational expression, strictly positive for all \(a\ge2,b\ge1\). This is a finite algebraic proof, not an asymptotic argument.

## Verification

Run `python3 verify.py` using only the Python standard library. The supplied checker enumerates every fixed-content binary word for \(3\le a+b\le13\) with \(a\ge2\), verifies the exact joint counts and covariance, checks adjacent two-by-two minors for \(2\le a\le64\), and checks all pairs of rows and columns for \(2\le a\le19\). It completed 2,304,064 exact assertions successfully. The checker does not certify an infinite family by enumeration; the preceding algebraic argument supplies the all-parameter result.

## Relationship to prior work

The fixed-composition enumeration of the number of success runs is classical, appearing in older runs-test work; the exact formula is reproduced in Balado and Silvestre (2026), Section 4.2, Eq. (201), with earlier attributions to Stevens (1939), Mood (1940), and Schuster (1994). Malandro (2011) studies counts and expectations of parts of prescribed sizes in integer compositions. These sources provide the starting combinatorial objects and some of their margins. The assertion made here is the specific likelihood-ratio/TP2 ordering of the *joint* count of one-runs and singleton one-runs under a fixed number of ones, together with its exact covariance. The known univariate run-count formula, an exact generating function, or the conditional mean alone does not state this two-statistic distributional order; obtaining it uses the explicit adjacent-row cross-product inequality above.

## Limitations

This result concerns fixed numbers of ones and zeros, uniform words, one-runs only, and likelihood-ratio order in their singleton count. It does not establish any ordering for longer run lengths, nonuniform Markov strings, or an arbitrary statistic of singleton locations. Total positivity of order greater than two is not claimed. Earlier general run-length literature might contain equivalent statements not identified in the inspected open texts; no claim of exhaustive historical priority is made.

## References

- Martin E. Malandro, *Integer compositions with part sizes not exceeding k*, first arXiv version August 1, 2011, https://arxiv.org/abs/1108.0337.
- Félix Balado and Guénolé C. M. Silvestre, *Systematic Enumeration of Fundamental Quantities Involving Runs in Binary Strings*, first arXiv version February 10, 2026, https://arxiv.org/abs/2602.10005; particularly Sections 4.2 and 8.
- A. M. Mood, *The Distribution Theory of Runs*, Annals of Mathematical Statistics 11 (1940), 367–392, https://doi.org/10.1214/aoms/1177731825.
- L. Ya. Savelyev and S. V. Balakin, *The joint distribution of the number of ones and the number of 1-runs in binary Markov sequences*, Discrete Mathematics and Applications 14 (2004), 353–372, https://doi.org/10.1163/1569392041938802.
