# A palette-driven two-step forcing threshold for clique windmills

## Finding

Let \(r\ge2\), \(m\ge1\) be integers, and let \(W_{r,m}=K_1\vee(mK_r)\) be the labelled clique windmill with \(rm+1\) vertices. Let \(Q\ge r+2\) be an integer number of named colours, **strictly more than the chromatic number** \(r+1\). For \(t=Q-1\), write \((a)_{\underline r}=a(a-1)\cdots(a-r+1)\) for \(a\ge r\) and \((a)_{\underline r}=0\) for \(0\le a<r\). Define

\[
S_{r,m}(t)=\sum_{j=0}^{t}(-1)^j\binom tj\bigl((t-j)_{\underline r}\bigr)^m.
\]

Let \(\mathcal F_{Q}(W_{r,m};z)\) enumerate partial initial assignments that can be completed to a *proper* \(Q\)-colouring by iterated compulsory-neighbour-colour forcing, with a term \(z^k\) for each assignment initially colouring \(k\) vertices. Then

\[
\boxed{\mathcal F_{Q}(W_{r,m};z)=Q S_{r,m}(Q-1)z^{rm}+Q\bigl((Q-1)_{\underline r}\bigr)^m z^{rm+1}.}
\]

No other coefficients occur. The minimum initial forcing-domain size is precisely

\[
\boxed{\begin{cases}rm,&r+2\le Q\le rm+1,\\rm+1,&Q\ge rm+2,\end{cases}}
\]

where the first interval is empty for \(m=1\). In the first regime the exact number of minimum seeds is \(Q S_{r,m}(Q-1)>0\); in the second it is \(Q((Q-1)_{\underline r})^m\). At \(Q=rm+1\), the former number simplifies to \((rm+1)!\), since every vertex except the hub must use a different colour.

When each named colour is chosen independently at each vertex with probability \(p\), and the blank state with probability \(s=1-Qp\) (\(0\le p\le1/Q\)), the forced-completion probability is

\[
\boxed{\operatorname{FC}_Q(W_{r,m};p)=Q\,p^{rm}\left[S_{r,m}(Q-1)s+\bigl((Q-1)_{\underline r}\bigr)^m p\right].}
\]

There is also a sharp limit law for the central forcing event. For fixed \(r\ge2\) and real \(c\), let \(t\to\infty\) and choose positive integers \(m=m_t\) satisfying \(rm/t-\log t\to c\). Draw a uniformly random proper \((t+1)\)-colouring of \(W_{r,m}\), delete its hub colour but keep all outer colours. The probability that the unique missing hub colour can be recovered by a **single legal force** converges to

\[
\boxed{\exp(-e^{-c}).}
\]

This coupon-coverage limit is included as a consequence of the exact graph-theoretic reduction, not claimed as a new general coupon-collector theorem.

## Assumptions and scope

All graphs and vertices are labelled; each of the \(m\) petals is an independent \(r\)-clique attached to the same hub. A partial colouring is successful only if an iteration of the local rule reaches a proper full colouring. Under the local rule, a blank vertex is assigned the sole colour absent from its already coloured neighbours if precisely one palette colour remains permissible. The outer vertices have degree \(r\) and the hub has degree \(rm\). Both \(Q\) and the graph parameters are quantified as above. A failed or illegal initial assignment is not counted. This theorem deliberately addresses only the **nonchromatic** palette range \(Q\ge r+2\): the chromatic-palette formula is an earlier, separate result.

## Proof

**Only the hub may initially be blank.** Since \(Q\ge r+2\), every outer vertex has degree \(r\le Q-2\). It can never see the required \(Q-1\) distinct neighbour colours, at any stage. Therefore every outer vertex must be assigned a colour initially in any successful partial colouring. This is the key structural change from the chromatic-palette regime.

**Case of a coloured hub.** Such an assignment is successful if and only if the entire initial assignment is a proper full \(Q\)-colouring. Choose the hub's colour in \(Q\) ways. Each petal must be injected into the \(Q-1\) remaining colours, independently in \((Q-1)_{\underline r}\) ways. Thus the number is \(Q((Q-1)_{\underline r})^m\), entirely at degree \(rm+1\).

**Case of a blank hub.** As all outer vertices are initially coloured, the hub can be forced exactly when its neighbours collectively use \(Q-1\) different colours. In that event the remaining colour is unique, does not appear on its neighbours, and produces a proper full colouring. Conversely, if fewer than \(Q-1\) distinct colours appear, no vertex is eligible for the first force. If all \(Q\) colours appear, no colour is permissible for the hub. Thus successful blank-hub seeds have precisely one palette colour missing and use every other colour, with the \(r\) vertices of each petal differently coloured.

Choose the absent colour in \(Q\) ways. The number of labelled assignments of the \(t=Q-1\) allowed colours to the \(m\) ordered \(r\)-petals that are injective within each petal and use *every* allowed colour is, by ordinary inclusion–exclusion over unused colours,

\[
\sum_{j=0}^{t}(-1)^j\binom tj ((t-j)_{\underline r})^m=S_{r,m}(t).
\]

Hence there are \(Q S_{r,m}(t)\) such seeds, all of degree \(rm\). The cases are disjoint and exhaustive, proving the polynomial. The probability formula multiplies the respective counts by \(p^{rm}s\) and \(p^{rm+1}\).

**Exact threshold.** The surjection count \(S_{r,m}(t)\) is positive exactly for \(r\le t\le rm\). Necessity follows because a petal uses \(r\) distinct colours and the total \(rm\) outer positions cannot use more than \(rm\) distinct colours. Sufficiency follows constructively: for every \(t\) in that interval, partition the \(t\) colours into \(m\) groups of size at most \(r\), cover each group with a distinct petal's slots, and fill any spare slots in that petal with other distinct palette colours. (One can arrange a partition with every group nonempty because \(m\le rm\), and empty groups are also permissible.) This yields a valid assignment with all \(t\) colours used. For \(t=rm\), the \(rm\) outer slots are a permutation of all colours, so \(Q S_{r,m}(rm)=Q(rm)!=(rm+1)!\). The asserted minimum sizes and multiplicities follow.

**Limit law.** Conditional on any chosen hub colour of a uniformly random proper \((t+1)\)-colouring, every petal independently contains an ordered uniform injection of \(r\) among the other \(t\) colours. The hub colour can be recovered from the coloured outer vertices exactly when all \(t\) colours are represented. If \(E_j\) denotes the event that a fixed \(j\)-set of these colours is completely absent, then

\[
\Pr(E_j)=\left(\frac{(t-j)_{\underline r}}{(t)_{\underline r}}\right)^{m}.
\]

For each fixed nonnegative integer \(j\), the hypothesis \(rm/t-\log t\to c\) and the product formula give

\[
\binom tj\Pr(E_j)\longrightarrow\frac{e^{-jc}}{j!},
\]

since \(\log[(t-j)_{\underline r}/(t)_{\underline r}]=-jr/t+O(t^{-2})\) for fixed \(r,j\). The finite Bonferroni upper and lower bounds on the probability that no colour is absent are the even and odd partial sums of its inclusion–exclusion series. Taking \(t\to\infty\) for each fixed truncation and then sending the truncation to infinity gives \(\sum_{j\ge0}(-1)^j e^{-jc}/j!=\exp(-e^{-c})\), as claimed.

## Verification

The standalone `verify.py` constructs each windmill directly from its graph edges. It enumerates every initial assignment from \(Q\) named colours plus blank, repeatedly applies the original compulsory-colour rule, verifies final properness, and independently computes the predicted two polynomial coefficients from inclusion–exclusion. Eight small cases, including \(Q>rm+1\) where blank-hub success is impossible, agree at every coefficient: \((r,m,Q)=(2,1,4),(2,2,4),(2,3,4),(2,2,5),(2,3,5),(2,2,6),(3,1,5),(3,2,5)\). Execute `python3 verify.py`; the marker is `VERIFY_OK nonchromatic_palettes`. These experiments do not prove the infinite symbolic result or the limit; those follow from the preceding arguments.

## Relationship to prior work

Farr introduced the random stepwise forced-colouring function, with general and computational-complexity results. A previous exact windmill calculation covers **only** the chromatic palette \(Q=r+1\); the present claim is disjoint, treating **every surplus palette size** \(Q\ge r+2\). The added colours qualitatively change local forcing, because outer vertices become permanently unforceable. The resulting full-colouring-versus-hub-only classification, sharp second palette threshold \(Q=rm+2\), and missing-colour coverage formula are not consequences of substituting a parameter into the chromatic-palette expression. Standard inclusion–exclusion and the classical coupon-collector limit provide counting and asymptotic tools, rather than independent claims of novelty. Comparisons with known complete multipartite and bounded-degree forced-colouring formulas concern different graph families or palettes. Historical priority beyond inspected and indexed literature is not independently established.

## Limitations

The full formula is for clique windmills with equally sized petals and surplus palettes; it does not claim a characterization of arbitrary block graphs or correlated random initial colours. The coupon-coverage limit assumes fixed petal size \(r\), uniform proper full colourings, and the stated joint growth scale. The limit is a classical occupancy consequence, not a new general probabilistic limit law. Mathematical and historical priority verification have not been performed independently.

## References

1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108, first public preprint 2026-09-15. https://arxiv.org/abs/2609.17108 .
2. *Exact forcing-colouring spectrum of clique windmills*, prior chromatic-palette theorem for \(Q=r+1\), as a related comparison. The formula is distinct from the surplus-palette claim here.
3. Classical inclusion–exclusion for surjections and the coupon-collector/occupancy Poisson limit are used as standard methods, not claimed as new.
