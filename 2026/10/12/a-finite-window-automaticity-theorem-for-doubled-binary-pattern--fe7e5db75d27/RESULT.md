# A finite-window automaticity theorem for doubled binary pattern progressions

## Finding

Let \(v=w0\) be any fixed binary pattern of length \(L\ge 2\) containing at least one \(1\). Put \(M=2^{L-1}\) and \(r=[w]_2\), where the bracket denotes the binary integer represented by the displayed word, including any initial zeros. For \(n\ge 0\), write \(g_v(n)\) for the parity of the number of occurrences of \(v\) in the conventional binary representation of \(n\), with the initial-zero convention stated below. Define
\[
 A_v(0,d)=\min\{j\ge1:g_v(jd)\ne g_v(0)\},\qquad
 t_v(d)=\min\{j\ge1:jd\equiv r\pmod M\},
\]
where the second minimum is \(\infty\) when no such integer exists. Then **for every integer \(d\ge1\)**,
\[
 \boxed{A_v(0,2d)=A_v(0,d)\ \Longleftrightarrow\ t_v(d)=\infty\ \text{or}\ A_v(0,d)<t_v(d).}
\]
The test is finite: \(t_v(d)=\infty\) precisely when \(\gcd(d,M)\nmid r\). Otherwise \(1\le t_v(d)\le M/\gcd(d,M)\le M\). Thus the full equality set has the explicit characterization
\[
 \begin{aligned}
 \mathcal D_v={}&\{d\ge1:\gcd(d,M)\nmid r\}\\
 &\cup\left\{d\ge1:\begin{array}{l}
 \exists j\in\{1,\ldots,M-1\}\text{ with } g_v(jd)=1,\\
 hd\not\equiv r\pmod M\text{ for every }1\le h\le j
 \end{array}\right\}.
 \end{aligned}
\]
For every fixed \(v\), this set is \(2\)-automatic, and membership of \(d\) can be determined in \(O_v(\log d)\) bit operations. Two examples are
\[
\mathcal D_{10}=\{d\ge1:2\mid d\},
\]
and
\[
\mathcal D_{100}=\{d\ge1:4\mid d\}\cup\{d\ge1:d\text{ odd and }g_{100}(d)=1\}.
\]

## Assumptions and scope

The fixed pattern \(v\) ends in \(0\), has length at least two, and contains at least one \(1\). If the pattern begins with \(z\) zeros, count its possibly overlapping occurrences in the word consisting of \(z\) zeros followed by the conventional binary expansion of \(n\); this is the usual convention for nonzero binary block-counting patterns. In particular \(g_v(0)=0\). The first-disagreement time \(A_v(0,d)\) is finite for such patterns and positive steps, by known finiteness results; our equality proof also compares any possible finite first disagreements directly. All quantifiers in the theorem range over positive integers unless indicated otherwise. The statement does not include the all-zero pattern.

## Proof

**1. Exact append-zero identity.** Appending a zero to the binary expansion of any \(n\ge1\) gives the expansion of \(2n\). Every occurrence of \(v\) not using the new last position is inherited unchanged, including the possible initial-zero padding. Exactly one additional occurrence ends at the appended zero when the immediately preceding \(L-1\) binary positions form \(w\). Because the padding supplies the required initial zeros, this suffix condition is equivalent to \(n\equiv r\pmod{2^{L-1}}\). Therefore, for all \(n\ge1\),
\[
 g_v(2n)=g_v(n)\oplus\mathbf 1_{\{n\equiv r\pmod M\}},
\]
where \(\oplus\) is addition modulo two. This identity is exact even when \(w\) begins with zeros.

**2. First-disagreement comparison.** Fix \(d\ge1\), and let \(t=t_v(d)\). If \(t=\infty\), the append identity applied to every \(n=jd\) shows \(g_v(2jd)=g_v(jd)\) for all \(j\ge1\), so the two first-disagreement times coincide. If \(t<\infty\), the two sequences agree at every step \(1\le j<t\) and take opposite values at step \(t\). If some \(j<t\) already satisfies \(g_v(jd)\ne g_v(0)=0\), their first disagreements are the same earlier step. If no such \(j\) exists, both sequences have color zero at steps smaller than \(t\), while at step \(t\) exactly one of their colors is one. Hence precisely one progression has first disagreement at \(t\), and the first-disagreement times cannot coincide. This proves both directions of the boxed equivalence.

**3. Uniform finite window.** Elementary linear congruence theory gives existence of \(jd\equiv r\pmod M\) if and only if \(\gcd(d,M)\mid r\). When it exists, the positive solution steps occupy one residue class modulo \(M/\gcd(d,M)\), so its least positive representative is at most \(M/\gcd(d,M)\). Since \(g_v(0)=0\), a disagreement before \(t\) is exactly a positive parity \(g_v(jd)=1\). Substitution into the equivalence yields the displayed fixed-window Boolean formula with \(j\le M-1\).

**4. Automaticity and complexity.** For each fixed multiplier \(j\in\{1,\ldots,M-1\}\), multiplication of the base-two integer \(d\) by \(j\) can be performed least-significant-digit first by a deterministic finite-state carry transducer: with incoming carry \(c\) and binary digit \(x\), output the residue of \(jx+c\) modulo two and update the carry to \(\lfloor(jx+c)/2\rfloor\). All carries belong to a finite set dependent on \(j\), and a final finite flush outputs the remaining carry. Parity of occurrences of the fixed block \(v\) is computed by a finite-state machine remembering at most \(L-1\) preceding digits and one parity bit; leading-zero conventions are enforced at the finite terminal flush. Consequently \(d\mapsto g_v(jd)\) is a \(2\)-automatic binary sequence. The congruences \(hd\equiv r\pmod M\) are regular because \(M\) is fixed. The displayed Boolean formula for \(\mathcal D_v\), formed by finitely many unions and intersections of these regular predicates, therefore defines a regular base-two language. For fixed \(v\), it takes a fixed number of \(O(\log d)\)-bit multiplications by constant integers and fixed-pattern parity evaluations, giving the claimed time bound.

**5. Small-pattern descriptions.** For \(v=10\), \(M=2,r=1\): odd steps trigger at \(t=1\), while even steps never trigger; therefore only even differences qualify. For \(v=100\), \(M=4,r=2\): multiples of four never trigger, differences congruent to two modulo four trigger immediately and fail, while for an odd difference the first trigger is \(t=2\); in this last case equality holds exactly when \(g_{100}(d)=1\).

## Verification

The standalone file `verify.py` implements two independent occurrence-parity scanners (conventional most-significant-first representation and reversed least-significant-first windows). It checks the append identity for all positive \(n\le512\) and all \(57\) qualifying patterns of lengths two through six, independently compares direct first-disagreement times along both step sizes for every \(1\le d\le159\), and checks the two illustrative exact descriptions for \(1\le d\le1000\). These are finite corroborations; the proof of the all-pattern, all-step result is Steps 1–5, not a finite extrapolation. The only runtime dependency is Python's standard library. Run `python3 verify.py`.

## Relationship to prior work

Bartosz Sobolewski's *On monochromatic arithmetic progressions in binary words associated with pattern sequences*, first circulated April 11, 2022, poses in its concluding **Problem 6** precisely the question of describing positive differences \(d\) with \(A_v(0,2d)=A_v(0,d)\) for a block ending in zero. That work establishes broader finiteness and upper bounds for monochromatic progressions and a different special case involving the Rudin–Shapiro sequence. Here, unlike those bounds, the append-zero identity yields an effective finite-window characterization for **each** qualifying pattern and the regularity of the entire set of differences.

Joshi and Rust study analogous arithmetic-progression quantities for Fibonacci, Thue–Morse, and Rudin–Shapiro words, without the all-pattern doubling criterion in their inspected discussion. Sobolewski's later work on additive differences of binary block-counting functions concerns another comparison operation. An equivalent unindexed treatment or an implicit derivation from broader automata theory cannot be ruled out; the present contribution is the explicit classification for this concrete open problem, not a claim of an entirely new automata method.

## Limitations

The theorem excludes all-zero patterns, uses only progressions **starting at zero**, and concerns precisely the equality of first-disagreement lengths for differences \(d\) and \(2d\). It makes no assertion about maximal progressions with arbitrary starting points, the distribution of \(A_v(0,d)\), or general automatic words not generated by binary block-occurrence parity. The fixed-parameter running-time constant can grow exponentially with the pattern length; it is not a uniform polynomial-in-pattern-length bound.

## References

1. B. Sobolewski, *On monochromatic arithmetic progressions in binary words associated with pattern sequences*, arXiv:2204.05287 (first submission 2022-04-11); *Theoretical Computer Science* 1018 (2024), article 114815, DOI:10.1016/j.tcs.2024.114815.
2. G. Joshi and D. Rust, *Monochromatic arithmetic progressions in the Fibonacci, Thue-Morse, and Rudin-Shapiro words*, arXiv:2501.05830.
3. B. Sobolewski, *On the behavior of binary block-counting functions under addition*, arXiv:2412.15851.
