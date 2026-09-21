# Exact capacity of window-two sliding-window dynamic frameproof codes

## Result

Let \(F_2(q)\) denote the maximum number of users supported by a \(q\)-ary sliding-window \(2\)-dynamic **frameproof** code in the sense of Paterson: pirate coalitions are unrestricted in size, and a valid pirate broadcast uses only nonunique marks.

For every \(q\ge 2\),
\[
\boxed{F_2(q)=\max_{1\le a\le q-1} a(q-a+1)
      =\left\lfloor\frac{(q+1)^2}{4}\right\rfloor.}
\]

Thus \(F_2(2)=2\). If \(q=2m+1\) is odd, the maximizing value is \(a=m+1\). If \(q=2m\ge4\) is even, both \(a=m\) and \(a=m+1\) attain the maximum.

This settles the window-length-two case of the general-variable-protection question posed for sliding-window dynamic frameproof codes.

## Definitions

At time \(j\), after pirate history \(\Xi_j=(\xi_1,\ldots,\xi_{j-1})\), let
\[
R_j(x)=\{u:D_j(\Xi_j,u)=x\}
\]
be the recipient class of symbol \(x\). A mark is *nonunique* when \(|R_j(x)|\ge2\). Paterson's valid pirate broadcasts use only nonunique marks. A user is framed over a window of length two if an innocent user receives both pirate marks in two consecutive segments.

## Upper bound

Set
\[
M(q)=\max_{1\le s\le q-1}s(q-s+1)
=\left\lfloor\frac{(q+1)^2}{4}\right\rfloor.
\]
Suppose, for contradiction, that a sliding-window \(2\)-dynamic frameproof code supports \(n>M(q)\) users. Since \(M(q)\ge q\), we have \(n>q\).

### Protection lemma

Fix any history consisting entirely of nonunique pirate marks, and suppose the current pirate mark \(\xi_j\) has recipient class \(C=R_j(\xi_j)\) of size \(s\ge2\). Then every user in \(C\) must receive a globally unique mark at time \(j+1\).

Indeed, suppose \(u\in C\) receives a nonunique mark \(y\) at time \(j+1\). Append \(y\) to the pirate history. Because every mark in the resulting prefix is nonunique, at each segment it is received by some user other than \(u\). Hence the coalition \(U\setminus\{u\}\) can produce that prefix, while \(u\) matches the pirate in the two consecutive segments \(j,j+1\). Since \(n>q\), every later allocation contains a nonunique mark, so this prefix can be extended indefinitely by nonunique marks. This frames \(u\), a contradiction.

Consequently, after broadcasting a class of size \(s\), at least \(s\) distinct alphabet symbols are consumed as unique marks in the next segment. Because these \(s\) marks must be globally unique, \(s\le q\); if \(s=q\), all \(q\) symbols are already occupied uniquely while \(n-q>0\) users still require marks, which is impossible. Hence \(s\le q-1\). The remaining \(n-s\) users occupy at most \(q-s\) symbols, so some nonunique recipient class in the next segment has size
\[
s'\ge \left\lceil\frac{n-s}{q-s}\right\rceil.
\]

Now \(n>M(q)\ge s(q-s+1)\), hence
\[
n-s>s(q-s),
\qquad\text{so}\qquad
s'>s.
\]
Starting from any nonunique mark and repeatedly choosing a largest nonunique recipient class therefore produces a strictly increasing sequence
\[
2\le s_1<s_2<s_3<\cdots\le q-1,
\]
which is impossible. Thus \(n\le M(q)\).

## Matching construction

Fix \(a\in\{1,\ldots,q-1\}\) and put
\[
n=a(q-a+1).
\]
In each segment choose a protected set \(P\) of exactly \(a\) users. Give the users in \(P\) \(a\) distinct unique symbols. Partition the remaining
\[
n-a=a(q-a)
\]
users into \(q-a\) classes of size \(a\), one class for each remaining symbol.

For the first segment choose \(P\) arbitrarily. After any valid pirate broadcast, its mark is nonunique, hence (when \(a\ge2\)) its recipient class is one of the ordinary size-\(a\) classes; use exactly that class as the protected set in the next segment. On histories that are not valid pirate histories, define the next protected set arbitrarily. If \(a=1\), every mark is unique and there is no valid pirate broadcast, so the code is trivially frameproof.

For \(a\ge2\), if a user matches the pirate in one segment then that user belongs to the protected set in the next segment and receives a unique mark there. A valid pirate broadcast cannot use that unique mark. Hence no user can match the pirate over two consecutive segments, so the scheme is a sliding-window \(2\)-dynamic frameproof code supporting \(a(q-a+1)\) users.

Maximizing this quadratic over integer \(a\) gives \(M(q)\), proving the theorem.

## Relation to prior literature

Paterson introduced sliding-window dynamic frameproof codes and proved optimality for several restricted families. Her general construction with parameters \(\alpha,\beta\) includes, at \(\beta=0\) and window length \(2\), the value
\[
\alpha(q-\alpha+1).
\]
The paper then explicitly asks whether fully general schemes, in which the number of protected users may vary with the segment and pirate history, can support more users. The theorem above shows that for window length \(2\) they cannot: optimizing the fixed-\(\alpha\) value already gives the unrestricted capacity.

The paper's unrestricted asymptotic upper bound is \(q^l+O(q^{l-1})\) for fixed \(l\); at \(l=2\), the exact value above sharpens this to \(\frac14q^2+O(q)\).

## Verification

A compact exhaustive sanity check of the explicit construction is included in `artifacts/verify_construction.py`. It enumerates all nonunique pirate choices through six segments for every \(q\le6\) and every \(1\le a<q\); all tested cases pass. This finite check is supplementary and is not used in the general proof.

## Originality and limitations

To the best of our knowledge, no later source located in searches under *sliding-window dynamic frameproof code*, *dynamic frameproof code*, window length two, and related frameproof terminology states this unrestricted exact formula. Paterson's paper explicitly leaves the general variable-protection problem open. A citation-index snapshot updated in 2026 lists five works citing the sliding-window paper; the directly frameproof-related later item located there concerns static wide-sense \(2\)-frameproof codes rather than feedback-dependent sliding-window schemes. Citation databases and keyword searches are not exhaustive, so the originality claim remains qualified.

The result is specific to window length \(2\) and to Paterson's unrestricted-coalition notion of *frameproof*. The upper-bound argument uses a coalition as large as \(U\setminus\{u\}\) and therefore does not establish the same capacity for sliding-window \(2\)-dynamic \(c\)-frameproof codes with a fixed small coalition bound \(c\).

## References

1. M. Paterson, “Sliding-window dynamic frameproof codes,” *Designs, Codes and Cryptography* 42(2), 195–212 (2007). https://doi.org/10.1007/s10623-006-9030-9
2. M. Paterson, “Sequential and dynamic frameproof codes,” *Designs, Codes and Cryptography* 42(3), 317–326 (2007). https://doi.org/10.1007/s10623-006-9037-2
3. J. Zhou and W. Zhou, “Wide-sense 2-frameproof codes,” *Designs, Codes and Cryptography* 88(12), 2507–2519 (2020). https://doi.org/10.1007/s10623-020-00797-w
