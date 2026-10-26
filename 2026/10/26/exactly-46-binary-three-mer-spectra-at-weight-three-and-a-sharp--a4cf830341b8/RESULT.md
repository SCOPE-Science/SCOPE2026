# Exactly 46 binary three-mer spectra at weight three and a sharp dominant fiber

## Finding

Let \(w\) range over all linear binary words of length \(n\ge3\) containing precisely three occurrences of \(1\). Observe the vector of multiplicities of **all eight contiguous length-three factors**, including overlapping factors. Then the number \(P_n\) of distinct observation vectors is

\[
(P_3,P_4,P_5,P_6,P_7,P_8,P_9,P_{10})=(1,4,9,16,27,35,42,45),\qquad P_n=46\quad(n\ge11).
\]

Consequently an error-free code restricted to this weight class and decoded from its length-three factor multiset has largest possible cardinality \(P_n\); the threshold for its eventual constant value is sharp.

For every \(n\ge18\), the **unique most ambiguous observation** has the exact fiber size
\[
M_n=\binom{n-8}{3}.
\]
Its preimages are exactly the words \(0^a1\,0^b1\,0^c1\,0^d\) for which \(a,b,c,d\ge2\). The threshold is sharp: at \(n=17\), this fiber contains \(84\) words, whereas a different fiber contains \(90\). Moreover,
\[
\frac{\binom{n-8}{3}}{\binom n3}\longrightarrow1.
\]
Thus almost all three-one words have the same observed trigram-count vector as their length tends to infinity.

## Assumptions and scope

Words are **linear rather than circular**, the alphabet is exactly \(\{0,1\}\), all three occurrences of \(1\) are distinct positional markers, and the observation retains multiplicities and order *within* a trigram but not the locations of trigrams. No initial or final symbols are supplied separately to the observer. There is no claim about arbitrary Hamming weight, longer reads, error correction, or uniqueness of reconstruction beyond this channel.

Write uniquely
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad a,b,c,d\in\mathbb Z_{\ge0},\quad a+b+c+d=N=n-3.
\]
For a gap quadruple define its truncated signature \(t=(\min(a,2),\min(b,2),\min(c,2),\min(d,2))\). The only trigrams involving \(1\), in the fixed order \((001,010,011,101,110,100,111)\), have a count vector \(F(t)\). The count for \(000\) equals \(n-2\) minus the sum of these seven counts; hence at a fixed length, equality of full observations is exactly equality of \(F(t)\).

## Proof

**Step 1 (local signature rule).** Let \(t=(a,b,c,d)\in\{0,1,2\}^4\), where these variables now mean *truncated* gaps. Directly counting the windows around the three marked letters yields
\[
\begin{aligned}
F_{001}&=[a=2]+[b=2]+[c=2],\\
F_{010}&=[a>0][b>0]+[b>0][c>0]+[c>0][d>0],\\
F_{011}&=[b=0][a>0]+[c=0][b>0],\\
F_{101}&=[b=1]+[c=1],\\
F_{110}&=[b=0][c>0]+[c=0][d>0],\\
F_{100}&=[b=2]+[c=2]+[d=2],\\
F_{111}&=[b=0][c=0].
\end{aligned}
\]
Here \([E]\) is \(1\) when \(E\) holds and otherwise \(0\). Every trigram including a marker is accounted for exactly once: an isolated marked letter contributes its left/two-sided/right windows when permitted by neighboring gap lengths, while zero gaps contribute \(011,110,111\) across adjacent markers. Every window consisting solely of zeros is determined by subtraction. Thus no information outside \(t\) and \(n\) influences the observed profile.

**Step 2 (exact fingerprint partition).** Apply the displayed rule to the complete finite domain \(\{0,1,2\}^4\) of \(81\) signatures. The exhaustive finite table `signature_certificate.csv` explicitly lists all \(81\) inputs and seven-count outputs; `profile_certificate.csv` groups equal outputs. There are exactly \(59\) distinct outputs. Among them \(46\) have at least one signature with an entry equal to \(2\) (persistent outputs), and \(13\) have only \(0,1\) signatures (transient outputs). The distribution of the **least** possible total gap sum for a persistent output is
\[
\begin{array}{c|rrrrrrr}
N&2&3&4&5&6&7&8\\\hline
\#\text{ newly available persistent outputs}&4&10&12&9&7&3&1.
\end{array}
\]
The \(13\) transient outputs occur only at respective gap totals \(N=0,1,2,3,4\), with multiplicities \((1,4,5,2,1)\). The reason for permanence is that any gap represented by \(2\) may be increased without changing the signature. A transient signature has no extensible gap and contributes only at its fixed sum. Summing the displayed disjoint categories at each \(N=n-3\) proves all values of \(P_n\) and the sharp stabilization at \(n=11\). The two CSV tables are a finite, inspectable certificate of each integer count, not merely a sampled word experiment.

**Step 3 (exact fiber polynomial).** For each fingerprint \(v\), let \(T_v=\{t:F(t)=v\}\). Set \(m(t)=\sum_i t_i\) and \(r(t)=\#\{i:t_i=2\}\). At gap total \(N\), each \(t\) contributes
\[
h_t(N)=\begin{cases}
0,&N<m(t),\\
\binom{N-m(t)+r(t)-1}{r(t)-1},&N\ge m(t),\ r(t)>0,\\
[N=m(t)],&r(t)=0.
\end{cases}
\]
Indeed the excess above the truncated value two can be independently allocated to the \(r(t)\) extensible gaps. The exact number of words sharing observation \(v\) is \(H_v(N)=\sum_{t\in T_v}h_t(N)\). This also independently determines all finite reconstruction fibers.

**Step 4 (sharp largest fiber for all long lengths).** The fingerprint \(v_*=(3,3,0,0,0,3,0)\) has exactly one signature: \((2,2,2,2)\). Thus \(H_{v_*}(N)=\binom{N-5}{3}\) for \(N\ge8\), and precisely the quadruples of gaps at least two realize it. Every other persistent fingerprint has only signatures with at most three entries equal to \(2\); therefore \(H_v(N)\) is a polynomial in \(N\) of degree at most \(2\), once \(N\ge15\). Transient profiles are absent there.

For each of the \(45\) other persistent fingerprints, put \(\Delta_v(N)=\binom{N-5}{3}-H_v(N)\). The last four columns of `profile_certificate.csv` give \(\Delta_v(15)\), \(\Delta_v(16)-\Delta_v(15)\), and the next two successive forward differences, all as exact integers. Their minima over the \(45\) rivals are, respectively,
\[
(10,23,8,1).
\]
Since \(\Delta_v\) is a cubic polynomial for \(N\ge15\), Newton's forward formula gives, for every integer \(h\ge0\),
\[
\Delta_v(15+h)=\sum_{j=0}^3\binom hj\,\delta^j\Delta_v(15)>0,
\]
where \(\delta^j\) denotes the corresponding forward difference. Each coefficient in the sum is nonnegative and the \(j=0\) coefficient strictly positive. Hence \(v_*\) is the **unique** maximizer for all \(N\ge15\), i.e. \(n\ge18\). Exact enumeration from the same complete fibers at \(N=14\) gives \(90>\binom{9}{3}=84\), establishing the sharp threshold. Finally \(\binom{n-8}{3}/\binom n3\to1\), proving asymptotic information collapse.

## Verification

Execute `python3 checker.py` from a directory containing the accompanying two CSV certificates. The checker reconstructs the \(81\)-row table and the \(59\) equivalence buckets using integer arithmetic, verifies the displayed formulas against **direct substring enumeration for all \(7^4=2401\) gap quadruples with each gap at most six**, independently enumerates all weight-three words through length \(28\), verifies profile counts for totals through \(39\), regenerates both complete certificates, and evaluates the exact four-forward-difference proof inequalities. The all-length result comes from the proved polynomial identity plus a finite exhaustive signature table, not from extrapolation of those finite tests.

## Relationship to prior work

Pevzner, Tang and Waterman (2001) use Eulerian paths in a de Bruijn graph to analyze assembly from fragment reads; this supplies the general reconstruction setting but not the specific fixed-weight-three profile count, its stabilization at \(46\), or the unique dominant fiber. Karhumäki, Puzynina, Rao and Whiteland (2016) treat \(k\)-abelian word equivalence and provide a general Eulerian graph formula for individual class cardinalities. Their stronger observational equivalence also records shorter factors and endpoints in the conventional definition, so it is not identical to **trigram counts alone**. Their general methods are important background but do not, in the inspected text, state this finite complete classification and sharp threshold. The 2008 Velvet paper gives the algorithmic context of de Bruijn assembly without these enumerations. The all-length results here are a specialized structural reduction using four gaps and \(81\) truncated states.

## Limitations

The principal originality uncertainty is an earlier equivalent enumeration under \(k\)-mer spectrum or \(k\)-abelian terminology. The abstract of the 2016 paper *k-Abelian Equivalence and Rationality* was available, but its full primary text was not available in this investigation; it discusses rationality of related counts and may contain relevant specializations not confirmed here. The present proof does not claim a novel general graph-counting technique, nor does it show that the exact number \(46\) persists for other weights or alphabets. All machine-generated CSV data are finite proof certificates whose completeness is justified by the \(3^4\) state decomposition; neither a finite word census nor a software run independently establishes the infinite theorem.

## References

1. P. A. Pevzner, H. Tang, M. S. Waterman, “An Eulerian path approach to DNA fragment assembly,” *Proceedings of the National Academy of Sciences* 98 (2001), 9748–9753; DOI `10.1073/pnas.171285098`. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC55524/ . First published August 14, 2001.
2. J. Karhumäki, S. Puzynina, M. Rao, M. A. Whiteland, “On cardinalities of k-abelian equivalence classes,” arXiv:1605.03319 (public May 11, 2016); open full text: https://www.utupub.fi/bitstreams/0a31fb4a-47af-408f-a0ee-95d5e81c906e/download .
3. D. R. Zerbino, E. Birney, “Velvet: Algorithms for de novo short read assembly using de Bruijn graphs,” *Genome Research* 18 (2008), 821–829; DOI `10.1101/gr.074492.107`.
4. J. Cassaigne, J. Karhumäki, S. Puzynina, M. A. Whiteland, “k-Abelian Equivalence and Rationality,” *Developments in Language Theory* (2016), abstract consulted; full text not independently inspected.
