# Three-adic renormalization of Abelian repetitions in a 2-binomial-cube-free binary word

## Finding

Let \(h(0)=001\) and \(h(1)=011\), and let \(z=h^\omega(0)\) be the infinite binary fixed point. For every integer \(k\ge 0\), put \(m=3^k\) and \(p=(m-1)/2\). Given any starting index \(i\ge0\), set
\[
q=\left\lfloor\frac{i+m-1-p}{m}\right\rfloor.
\]
For every integer \(j\ge0\), the number of ones in the indicated factor is exactly
\[
\#_1\bigl(z[i+jm:i+(j+1)m)\bigr)=\frac{m-1}{2}+z_{q+j}.
\]
In particular, the complete sequence of length-\(3^k\) window Parikh vectors, sampled at strides of \(3^k\) from any offset, is a two-symbol recoding of the original infinite word. An adjacent pair of such windows is an Abelian square precisely when \(z_q=z_{q+1}\). No three such consecutive windows have equal Parikh vectors: **the fixed point contains no Abelian cubes whose block length is a power of three**. These conclusions hold at every position and at every nonnegative substitution scale, including \(k=0\).

Moreover, write \(E_t=\mathbf 1_{\{z_t=z_{t+1}\}}\). Then for every \(r\ge0\),
\[
(E_{3r},E_{3r+1},E_{3r+2})=(1-z_r,z_r,0).
\]
Consequently, at every fixed power-of-three block length the natural density (among starting positions) of Abelian squares is exactly \(1/3\); the density of Abelian cubes of that block length is zero. Each of the two possible length-\(3^k\) window Parikh vectors occurs with natural density \(1/2\).

## Assumptions and scope

A factor \(z[u:v)\) comprises the indices \(u,u+1,\ldots,v-1\); all positions and indices are nonnegative integers, and \(\#_1\) counts occurrences of the symbol \(1\). An Abelian \(r\)-power of block length \(m\) consists of \(r\) consecutive length-\(m\) factors having identical symbol-count vectors. A binary block's Parikh vector is specified uniquely by its length and number of ones. Densities refer to asymptotic proportions of starting indices \(i=0,\ldots,N-1\) as \(N\to\infty\), with fixed \(k\). No assertion about the existence or absence of Abelian cubes at block lengths that are not powers of three is included.

## Proof

**Step 1: A digit recursion.** The substitution immediately gives
\[
z_{3a}=0,\qquad z_{3a+1}=z_a,\qquad z_{3a+2}=1\quad(a\ge0).
\]
This also proves that every three consecutive symbols of \(z\) include at least one zero and at least one one: any three consecutive positions contain a position congruent to \(0\) and another congruent to \(2\) modulo three. Thus \(z\) contains neither \(000\) nor \(111\).

**Step 2: The unique free residue.** Fix \(k\ge0\), \(m=3^k\), and \(p=(m-1)/2\). In base three, \(p\) consists of \(k\) digits equal to \(1\). For an arbitrary block index \(a\ge0\), repeatedly apply the digit recursion to \(z_{ma+r}\), \(0\le r<m\). If \(r=p\), each recursion selects the central child, so \(z_{ma+p}=z_a\). If \(r\ne p\), the first (least-significant) ternary digit of \(r\) that is not \(1\) fixes \(z_{ma+r}\) to \(0\) when that digit is \(0\), or to \(1\) when it is \(2\), independently of \(a\). Reflecting residues via \(r\mapsto m-1-r\) swaps digits \(0\) and \(2\), and leaves each digit \(1\) unchanged. It therefore pairs the \(m-1\) noncentral residues into exactly \((m-1)/2\) constant zeros and \((m-1)/2\) constant ones. It follows that
\[
\#_1(z[ma:(a+1)m))=\frac{m-1}{2}+z_a.
\]
The same residue argument works for **arbitrary** length-\(m\) intervals, not just aligned ones. Such an interval contains exactly one index congruent to \(p\pmod m\), namely \(mq+p\), where
\[
q=\left\lceil\frac{i-p}{m}\right\rceil
=\left\lfloor\frac{i+m-1-p}{m}\right\rfloor.
\]
Its other \(m-1\) indices contain every noncentral residue exactly once. Therefore \(\#_1(z[i:i+m))=(m-1)/2+z_q\). For the interval starting \(i+jm\), its central index lies in the next aligned block, with index \(q+j\). This proves the stated exact window formula for every \(j\ge0\).

**Step 3: Abelian repetition classification.** At fixed length \(m\), equality of the two-letter Parikh vectors is exactly equality of their numbers of ones. Thus for \(r\ge2\), the consecutive \(r\) windows from \(i\) form an Abelian \(r\)-power if and only if \(z_q=z_{q+1}=\cdots=z_{q+r-1}\). Step 1 rules this out for \(r\ge3\), giving the all-position, all-scale Abelian-cube prohibition. For \(r=2\), equality is \(E_q=1\). Using Step 1 at the three possible residues gives
\[
E_{3a}=1-z_a,\qquad E_{3a+1}=z_a,\qquad E_{3a+2}=0.
\]
Therefore exactly one of every three consecutive \(E\) values, starting at a multiple of three, equals \(1\); its prefix frequency has discrepancy at most two from \(1/3\). For fixed \(m\), as the starting position \(i\) ranges over successive integers, the index \(q=\lfloor(i+m-1-p)/m\rfloor\) runs through successive integers, each repeated exactly \(m\) times, apart from a bounded initial truncation. Hence the density of starting positions yielding Abelian squares of block length \(m\) is exactly \(1/3\), and no Abelian cube of that block length occurs.

**Step 4: The two Parikh-vector frequencies.** Let \(F(N)=\sum_{a=0}^{N-1}z_a\). Step 1 implies
\[
F(3a)=a+F(a),\quad F(3a+1)=a+F(a),\quad
F(3a+2)=a+F(a)+z_a.
\]
Consequently \(\lvert 2F(N)-N\rvert=O(1+\log N)\) by repeated reduction of \(N\) to \(\lfloor N/3\rfloor\), and \(z\) has asymptotic symbol frequency \(1/2\). For fixed \(m\), the window formula transfers these frequencies to the low-ones and high-ones Parikh vectors, proving a natural density of \(1/2\) for each.

## Verification

The included standalone file `check_threeadic.py` independently generates \(h^{10}(0)\) by literal substitution, then verifies its 59,049 symbols against an integer digit-recursion implementation. It checks the window formula, adjacent-square indicators, and the absence of Abelian cubes for \(k=0,1,\ldots,6\) at 6,000 starting positions per scale (42,000 windows). It separately checks 770 instances of the exact \(E\)-recursion. All assertions passed with exact integer arithmetic. This finite experiment is a regression check, not a substitute for the proof for every \(k\) and every starting position.

## Relationship to prior work

Rao, Rigo and Salimov constructed the fixed point of \(0\mapsto001\), \(1\mapsto011\) while studying avoidance of 2-binomial squares and cubes [1]. Their established avoidance of **2-binomial cubes** does not imply avoidance of the weaker Abelian cubes, because Abelian equality requires only letter counts; it therefore does not entail the exact three-adic window identity, its square-occurrence density, or the precise scale-restricted Abelian-cube statement. The construction and its established stronger-type avoidance are credited to [1]. The general bounded-Abelian-complexity and avoidance setting appears in [2]. This result is a structural analysis of the specific older substitution across all powers of its uniform length, not a claim to invent the fixed point or solve its Abelian-cube spectrum at other lengths.

## Limitations

The finding concerns **only** block lengths equal to a nonnegative integer power of three; other Abelian-cube block lengths are not classified. It concerns an infinite fixed point, not arbitrary factors of other substitutions. The finite checks are not an independent formal proof or a certification of priority. Historical-priority overlap under alternate terminology remains possible, especially in studies of uniform substitutions and Abelian-complexity sequences.

## References

[1] M. Rao, M. Rigo and P. Salimov, *Avoiding 2-binomial squares and cubes*, arXiv:1310.4743v1, first posted 2013-10-17, https://arxiv.org/abs/1310.4743. Relevant primary result and fixed-point definition in the preprint's Section 3.

[2] J. Cassaigne, G. Richomme, K. Saari and L. Q. Zamboni, *Avoiding Abelian Powers in Binary Words with Bounded Abelian Complexity*, arXiv:1005.2514v1, first posted 2010-05-14, https://arxiv.org/abs/1005.2514.
