# Exact three-to-five real-fiber valence transition in a harmonic Landau shear

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). For every \(M>1\) define the bounded harmonic mapping of Borovikov [1]
\[
F_M(z)=z+i(M-1)\frac{2}{\pi}\operatorname{Arg}\left(\frac{1-z^2}{1+z^2}\right),\qquad z\in\mathbb D,
\]
where the argument takes values in \((-\pi/2,\pi/2)\). For each real target \(t\) set
\[
N_M(t)=\#\{z\in\mathbb D:F_M(z)=t\}.
\]
The **exact maximal number of distinct preimages of a real target** is
\[
\boxed{\max_{t\in\mathbb R}N_M(t)=
\begin{cases}
3,&1<M\le 1+\dfrac{\pi}{\sqrt{\pi^2+4}},\\[4pt]
5,&M>1+\dfrac{\pi}{\sqrt{\pi^2+4}}.
\end{cases}}
\]
In particular, no real target has more than five preimages; for every parameter above the sharp threshold a real target has five **distinct interior** preimages. The transition value is approximately \(1.8435636080687687\).

## Assumptions and scope
The source mapping is harmonic and has \(F_M(0)=0\), \(\lambda_{F_M}(0)=1\), and \(|F_M(z)|<M\) on \(\mathbb D\) [1, Section 2]. The theorem concerns only targets in \(\mathbb R\), not the full-plane maximal valence. The count is of distinct solutions, not multiplicities at critical points. Every parameter \(M>1\), including equality at the transition, is covered.

## Proof
Write \(m=M-1>0\) and \(z=x+iy\). The explicit real-coordinate expression in [1, Eq. (6)] gives
\[
\operatorname{Re}F_M(x+iy)=x,\quad
\operatorname{Im}F_M(x+iy)=y-mg_x(y),\quad
g_x(y)=\frac2\pi\arctan\frac{4xy}{1-(x^2+y^2)^2}
\]
for \(x>0\), \(0<y<b_x:=\sqrt{1-x^2}\). Since the imaginary part of the harmonic correction has the sign opposite to \(xy\), negative real targets and target zero have only their trivial real preimage. For a target \(x\in(0,1)\), the real point \(z=x\) is always a preimage; all other preimages occur as conjugate pairs \(x\pm iy\). Let
\[
\mu_x(y)=\frac{y}{g_x(y)}\qquad(0<y<b_x).
\]
Thus \(N_M(x)=1+2n_x(m)\), where \(n_x(m)\) counts the solutions of \(\mu_x(y)=m\) on the *open* vertical interval. The endpoint limits are
\[
\mu_x(0):=\lim_{y\downarrow0}\mu_x(y)=\frac{\pi(1-x^4)}{8x},
\qquad \mu_x(b_x):=\lim_{y\uparrow b_x}\mu_x(y)=b_x.
\tag{1}
\]
Both endpoint values refer to limits, never preimages on the boundary.

**Unimodality lemma.** For each fixed \(0<x<1\), the function \(\mu_x\) is initially strictly increasing and either continues strictly increasing or increases up to one interior maximum and then strictly decreases. In particular every horizontal level is attained at most twice. To prove this, put \(p(z)=z/(1-z^4)\). Differentiation of the analytic logarithm defining the harmonic function gives
\[
g_x'(y)=\frac8\pi\operatorname{Re}p(x+iy),\qquad
g_x''(y)=-\frac8\pi\operatorname{Im}p'(x+iy).
\]
Writing \(w=z^4\), direct complex rational algebra yields the exact identity
\[
\operatorname{Im}p'(z)
=\frac{(5-2\operatorname{Re}w-3|w|^2)\operatorname{Im}w}{|1-w|^4},
\quad p'(z)=\frac{1+3z^4}{(1-z^4)^2}.
\tag{2}
\]
The parenthesis is strictly positive for \(|w|<1\), since it is at least \(5-2|w|-3|w|^2>0\). For \(x,y>0\), \(\operatorname{Im}(x+iy)^4=4xy(x^2-y^2)\). Therefore \(g_x''<0\) while \(y<x\), and \(g_x''>0\) while \(y>x\), whenever these ranges lie inside the disk. Define
\[
H_x(y)=g_x(y)-yg_x'(y).
\]
Since \(H_x(0)=0\), \(H_x'(y)=-yg_x''(y)\) is first positive and afterwards negative, while \(\mu_x'(y)=H_x(y)/g_x(y)^2\). Consequently \(H_x\) starts positive and can cross zero at most once, from positive to negative. This proves unimodality and \(N_M(t)\le5\) for every real \(t\).

**The sharp threshold.** The endpoint derivative is obtained from the arctangent expression by using \(1-(x^2+y^2)^2\to0\):
\[
g_x(b_x)=1,\qquad g_x'(b_x)=\frac{2}{\pi x},\qquad
H_x(b_x)=1-\frac{2b_x}{\pi x}.
\tag{3}
\]
Set
\[
x_c=\frac2{\sqrt{\pi^2+4}},\qquad
m_c=\frac\pi{\sqrt{\pi^2+4}}.
\]
Then \(x_c^2+m_c^2=1\), and Eq. (3), together with the unimodality lemma, says that \(\mu_x\) is strictly increasing throughout its interval when \(x\ge x_c\). If \(0<m\le m_c\) put \(x_b=\sqrt{1-m^2}\ge x_c\). For \(x\ge x_b\), the function is increasing, so \(\mu_x(y)=m\) has at most one interior solution. For \(x<x_b\), its boundary limit \(\mu_x(b_x)=b_x>m\); an initially increasing function with at most one interior maximum and terminal value above \(m\) can again meet level \(m\) at most once. Hence \(N_M(t)\le3\) when \(m\le m_c\).

This upper bound is achieved. Indeed \(\mu_x(0)=\pi(1/x-x^3)/8\) is strictly decreasing from infinity to zero, so for each \(m>0\) there is exactly one \(r\in(0,1)\) with \(\mu_r(0)=m\). For \(0<m\le m_c\),
\[
\frac{\mu_{x_b}(0)}m
=\frac{\pi m(2-m^2)}{8\sqrt{1-m^2}}
\le\frac{\pi^2(\pi^2+8)}{16(\pi^2+4)}<1.
\tag{4}
\]
The first inequality follows because the displayed ratio increases with \(m\in(0,1)\): its derivative has the positive factor \(2-3m^2+2m^4\). The last strict inequality follows, for example, from \(\pi^2<10\). Therefore \(r<x_b\). Choose \(x\in(r,x_b)\): by (1), \(\mu_x(0)<m<\mu_x(b_x)\). Continuity gives at least one interior solution; the upper bound gives exactly one. Thus the maximal real-fiber count is three in this regime.

Now suppose \(m>m_c\). For \(m\ge1\), take the unique \(r\) with \(\mu_r(0)=m\). Since \(H_r>0\) just above zero, \(\mu_r(y)>m\) at some small interior \(y\), whereas \(\mu_r(b_r)=b_r<1\le m\). Replacing \(r\) by a sufficiently nearby \(x>r\) preserves the strict interior inequality but makes both endpoint limits smaller than \(m\). By continuity and unimodality, \(\mu_x(y)=m\) then has two distinct interior solutions.

If \(m_c<m<1\), again put \(x_b=\sqrt{1-m^2}<x_c\). If \(r\ge x_b\), the preceding perturbation argument works because \(b_r\le m\). If \(r<x_b\), take \(x=x_b\). Then \(\mu_{x_b}(0)<m=\mu_{x_b}(b_{x_b})\), while \(H_{x_b}(b_{x_b})<0\) by (3), so \(\mu_{x_b}(y)>m\) for \(y\) sufficiently close to its endpoint from below. Increase \(x\) slightly beyond \(x_b\), retaining this strict interior inequality while obtaining \(\mu_x(0)<m\) and \(\mu_x(b_x)<m\). Again there are exactly two distinct interior solutions. Along with the real preimage \(z=x\) and both conjugates of each positive solution, they give five distinct points of \(\mathbb D\) mapping to \(x\). This proves the second regime and completes the proof. \(\square\)

## Verification
The attached standalone `verify_real_fibers.py` numerically checks the transition value, the critical comparison in (4), and explicit *distinct* interior quintuple fibers for \(M=1.9\), \(M=2\), and \(M=4\); it additionally samples the three-preimage regime. The script's finite samples are not an exhaustive proof. The global upper bound and sharp threshold follow from the exact sign identity (2), boundary identity (3), and the continuity arguments above. To reproduce, run `python3 verify_real_fibers.py` with a standard Python 3 installation.

## Relationship to prior work
Borovikov [1] introduced the exact family and analyzed a real-axis Jacobian zero to disprove the Liu–Luo–Luo Landau-radius conjecture for sufficiently large \(M\). The present theorem asks a different question: the **maximal cardinality of a complete real-target fiber** throughout all \(M>1\). A zero Jacobian or a sharp centered injectivity radius alone does not determine whether a target has three or five distinct preimages; Eq. (2) provides the missing global fiber control. The earlier bounded-harmonic radius estimates [2,3] concern injectivity disks or coefficient conditions rather than five-preimage fiber counts.

## Limitations
Only real target fibers of this particular explicit family are classified. No assertion is made about the largest fiber over arbitrary complex targets, the global mapping degree, the sharp radius for all bounded harmonic maps, or a universality of the threshold. The small collection of numerical examples is corroborative, not a substitute for the proof. Equivalence with an unindexed analysis of this specific real-fiber problem remains a literature risk. Independent mathematical audit has not been performed.

## References
[1] M. Borovikov, *A Counterexample to the Liu–Luo–Luo Conjecture on the Harmonic Landau Radius*, arXiv:2609.39676v1 (first posted 2026-09-30), especially Eqs. (5)–(13), https://arxiv.org/abs/2609.39676.

[2] D. Kalaj, S. Ponnusamy and M. Vuorinen, *Radius of Close-to-convexity and Fully Starlikeness of Harmonic Mappings*, arXiv:1107.0610 (2011 preprint), https://arxiv.org/abs/1107.0610.

[3] M.-S. Liu, L.-F. Luo and X. Luo, *Landau–Bloch type theorems for strongly bounded harmonic mappings*, Monatsh. Math. 191 (2020), 175–185; theorem summarized in [1, p. 2].
