# Starting-player parity reversal in the domatic game on \(K_{1,1,n}\)
## Finding
For every integer \(n\ge 2\), let \(G_n=K_{1,1,n}=K_2\vee\overline{K_n}\). In the Hartnell--Rall domatic number game, \[\operatorname{dom}_g(G_n)=\begin{cases}2,&n\text{ odd},\\1,&n\text{ even},\end{cases}\qquad \operatorname{dom}^\prime_g(G_n)=\begin{cases}1,&n\text{ odd},\\2,&n\text{ even}.\end{cases}\] Moreover \(\operatorname{dom}(G_n)=3\). Thus for every \(n\ge2\), exactly one of the two starting-player versions has game value \(2\) and the other has value \(1\), with the roles reversed by the parity of \(n\).

Equivalently, on the split graph \(K_2\vee\overline{K_n}\), changing the starting player reverses the two-color outcome whenever the parity of \(n\) changes. The ordinary domatic number remains \(3\) throughout the family.

## Assumptions and scope
The graph is finite and simple. Write its two singleton-part vertices as \(u,v\), and let \(W\) be the independent part of size \(n\). A play uses the domatic number game of Hartnell and Rall: players alternately assign a palette color to an uncolored vertex; Alice wins exactly when every final color class is a dominating set. The quantities \(\operatorname{dom}_g\) and \(\operatorname{dom}^\prime_g\) denote the largest palette sizes for which Alice wins when Alice and Bob, respectively, move first.

For a completed two-coloring of \(G_n\), a color class is dominating exactly when it contains \(u\) or \(v\), or when it is all of \(W\). Hence Alice wins a two-color play exactly when either \(u\) and \(v\) receive different colors, or they receive the same color and every vertex of \(W\) receives the opposite color.

## Proof
The minimum degree is \(2\). Hartnell and Rall's even-minimum-degree upper bound therefore gives
\[
\operatorname{dom}_g(G_n),\operatorname{dom}^\prime_g(G_n)\le 2.
\]
Thus it suffices to decide the two-color game; one color is always winnable because the unique color class is the whole vertex set.

Suppose first that Alice starts and \(n\) is odd. Alice colors one vertex of \(W\). She then pairs the remaining \(n-1\) vertices of \(W\) arbitrarily and pairs \(u\) with \(v\). After every Bob move, Alice immediately colors the mate in the same pair. On the pair \({u,v}\) she chooses the color opposite Bob's. The pairing is legal because \(n-1\) is even. At the end \(u\) and \(v\) have different colors, so both color classes dominate. Therefore \(\operatorname{dom}_g(G_n)=2\) for odd \(n\).

Now let Alice start and \(n\) be even. Bob wins the two-color game. If Alice first colors one of \(u,v\) with color \(c\), Bob colors the other universal vertex with the same color. Alice is then first on the even set \(W\); Bob can ensure that some vertex of \(W\) receives color \(c\), so \(W\) is not monochromatic in the opposite color. If instead Alice first colors a vertex of \(W\), Bob colors a second vertex of \(W\) with the opposite color. The set \(W\) is now permanently mixed. The remaining \(n-2\) vertices of \(W\) can be paired, together with the pair \({u,v}\). Bob answers every subsequent Alice move in its pair, and on \({u,v}\) uses Alice's color. Thus \(u\) and \(v\) finish with the same color while \(W\) is mixed, so Alice loses. Hence \(\operatorname{dom}_g(G_n)=1\) for even \(n\).

Suppose next that Bob starts and \(n\) is even. Pair \(u\) with \(v\) and pair all vertices of \(W\). Alice answers each Bob move at the mate of that vertex; on \({u,v}\) she uses the opposite color. This forces the two universal vertices to receive different colors, so Alice wins and \(\operatorname{dom}^\prime_g(G_n)=2\).

Finally let Bob start and \(n\) be odd. Since \(n\ge2\), in this case \(n\ge3\). Bob first colors a vertex \(w_0\in W\) with color \(1\). If Alice colors a universal vertex next, Bob colors the other universal vertex with the same color. If that color is \(1\), the existing color-1 vertex in \(W\) already prevents \(W\) from being all color \(2\); if that color is \(2\), Bob ensures that some remaining vertex of \(W\) is colored \(2\). In either case the terminal characterization excludes an Alice win. If Alice's second move is instead in \(W\), Bob uses his next move in \(W\) so that the three already colored vertices of \(W\) include both colors. There remain an even number of vertices: the \(n-3\) uncolored vertices of \(W\) plus \(u,v\). Pair the remaining vertices, with \(u\) paired to \(v\); Bob answers every Alice move in its pair and uses the same color on \({u,v}\). Then \(W\) is mixed and \(u,v\) have the same color, so Alice loses. Therefore \(\operatorname{dom}^\prime_g(G_n)=1\) for odd \(n\).

For the ordinary domatic number, the three sets \({u}\), \({v}\), and \(W\) are dominating, while the standard bound \(\operatorname{dom}(G_n)\le\delta(G_n)+1=3\) gives equality.

## Verification
The accompanying `verify.py` constructs \(K_{1,1,n}\) directly, evaluates domination from adjacency, exhausts every terminal two-coloring to verify the terminal characterization, and solves both starting-player games by exact minimax with memoization for \(2\le n\le7\). It also checks the explicit three-class ordinary domatic partition. Running `python3 verify.py` produces the archived `verification_output.txt`.

This finite computation is a stress test only. The theorem for all \(n\ge2\) follows from the pairing strategies and the cited general upper bound.

## Relationship to prior work
Hartnell and Rall introduced the domatic number game and proved, among other results, the exact game values of complete bipartite graphs. Their complete-bipartite theorem does not apply to \(K_{1,1,n}\), which is complete tripartite and contains a triangle. The same paper's even-minimum-degree bound supplies the sharp palette upper bound used above.

A later paper of English and Swan develops further general bounds and starting-player comparisons for the domatic game. Searches of that paper and targeted searches for complete tripartite, split-graph, and \(K_{1,1,n}\) formulations did not locate the parity-reversal classification above.

## Limitations
The theorem is confined to the one-parameter family \(K_{1,1,n}\). It does not classify the game on arbitrary complete multipartite or split graphs. The originality assessment is based on inspected primary sources and targeted semantic and bibliographic searches; incomplete indexing or inaccessible literature remains a residual risk. Independent audit has not been performed.

## References
1. Hartnell and Rall, *The domatic number game played on graphs*, arXiv:2508.10754, first public 2025-08-14; Ars Combinatoria 165, DOI 10.61091/ars165-03.
2. English and Swan, *On the Domatic Game*, arXiv:2603.13522, first public 2026-03-13.
