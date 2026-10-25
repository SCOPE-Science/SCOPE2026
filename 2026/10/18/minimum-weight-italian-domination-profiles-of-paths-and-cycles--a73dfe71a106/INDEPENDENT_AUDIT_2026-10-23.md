# Independent mathematical audit

## correctness

PASS

Write z/o/t for numbers of labels 0/1/2 and w=o+2t. For max-degree-two paths/cycles, each zero needs two units of neighbor weight, giving 2z<=2w and t<=2w-n. For n odd this bounds twos by <=1 at minimum; for n even paths by <=2. For zero twos the zeros form an independent set (avoiding path endpoints), whose maximum independent subsets yield unique long odd-path minimizers, m binary even-path minima, two alternating even-cycle minima and n odd-cycle minima. For one 2, its support is forced next to the unique zero endpoint of an even path giving two reflected patterns; P3 adds 020, C3 adds three rotations of 200; on longer odd paths/Cycles one 2 cannot cover two required zero endpoints or adjacent zero pair. For two 2s equality forces the special P6 word 020020, no other even path. Hence exact leading coefficients: paths odd 1 except P3=2, paths even n/2+2 except P6=n/2+3; cycles C3=6, even >=4 gives 2, odd>=5 gives n. Independently enumerated every 3-state labeling for paths 1..9 and cycles 3..9, including P6 optimum=4,count=6 and C3 optimum=2,count=6. Finite tests corroborate this general proof, not replace it.

## originality

PASS

Best-of-knowledge distinct contribution after direct comparison with relevant same-invariant primary results, strong alternatives, indexed tables and a Resultary semantic search (Italian domination polynomial paths cycles minimum coefficient count minimizers). Known minimum values, feasibility reductions, algorithms and finite tables are credited, while the claimed additional structural enumeration is assessed separately. Unread high-relevance literature and alternative indexing are retained as residual risks, not silently treated as absence.

## value

PASS

The bottom coefficient of a natural domination polynomial directly quantifies optimum-label diversity, and the full structural classification explains a nontrivial parity pattern and an isolated P6 two-twos exception. Although the full coefficients are algorithmically computable from prior dynamic programs, a closed all-order edge coefficient and classification is a reusable exact mathematical fact rather than a tiny arbitrary table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
